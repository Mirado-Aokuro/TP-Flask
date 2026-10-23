taches = [
 {"id": 1, "titre": "Réviser les décorateurs",
 "priorite": "haute", "terminee": False},
 {"id": 2, "titre": "Installer Flask",
 "priorite": "normale", "terminee": True},
 {"id": 3, "titre": "Lire la doc Jinja2",
 "priorite": "basse", "terminee": False},
]

from urllib import request

from flask import Flask, flash
from flask import render_template
from flask import Flask, render_template, request
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.secret_key = "efbc09971804f7ca178a28147e5db4870469e42fa05338d2368b002d9c237818"

@app.route("/")
def index():
    return render_template("taches.html", taches=taches) 

@app.route("/taches/<int:id>")

def tache(id):
    print(type(id), id)
    for t in taches:
        if t["id"] == id:
            return t["titre"]
    return "Tâche introuvable"


@app.route("/taches/ajouter", methods=["GET", "POST"])
def ajouter():
    if request.method == "POST":
        titre = request.form["titre"].strip()
        priorite = request.form.get("priorite", "normale")
        priorites_valides = ["basse", "normale", "haute"]
        if not titre or len(titre) > 80 or priorite not in priorites_valides:
            return render_template("ajouter.html")
        nouvel_id = max((t["id"] for t in taches), default=0) + 1
        taches.append({"id": nouvel_id, "titre": titre,
            "priorite": priorite, "terminee": False})
        flash("Tâche ajoutée")
        return redirect(url_for("index"))
    return render_template("ajouter.html")


@app.post("/taches/<int:id>/terminer")
def terminer_tache(id):
    for t in taches:
        if t["id"] == id:
            t["terminee"] = True
            break
    return redirect(url_for("index"))

@app.post("/taches/<int:id>/supprimer")
def supprimer_tache(id):
    global taches
    taches = [t for t in taches if t["id"] != id]
    return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404



@app.route("/api/taches")
def api_taches():
    return taches