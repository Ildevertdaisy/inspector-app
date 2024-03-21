
from flask import Flask, render_template
import requests


from dotenv import load_dotenv
import os


# Utiliser les variables d'environnement

FILE_SERVER = os.environ.get("FILE_SERVER")

app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/dashboard")
def get_dashboard():
    # Utiliser le module requests pour communiquer avec le serveur des fichiers qui tourne dans un autre serveur  
    request = requests.get(f"{FILE_SERVER}/files")
    data = request.json()["files"]
    return render_template("dashboard.html", files=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)