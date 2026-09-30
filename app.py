# app.py
# ------------------------------------------------------------
# Point d'entrée de l'application Flask du site vitrine CIRIM.
# Ce fichier ne fait que déclarer les routes (les adresses du
# site) et dire à Flask quelle page HTML afficher pour chacune.
# Il n'y a pas de base de données ni de formulaire : chaque page
# est simplement un fichier HTML du dossier templates/.
# ------------------------------------------------------------

from flask import Flask, render_template

# On crée l'application Flask.
# __name__ permet à Flask de savoir où se trouve le projet
# pour retrouver automatiquement les dossiers templates/ et static/.
app = Flask(__name__)

# Informations de l'entreprise.
# Elles sont regroupées ici pour être facilement modifiables
# et réutilisées sur toutes les pages (voir templates/base.html).
COORDONNEES = {
    "nom_entreprise": "CIRIM",
    "nom_complet": "Conseil en Ingénierie Risques Industriels et Maintenance",
    "fondateur": "Sekou Amadou GOITA",
    "telephone": "+223 71 24 09 19",
    "telephone_lien": "+33765736364",  # format international pour les liens cliquables
    "whatsapp_lien": "33765736364",    # format attendu par wa.me (sans le +)
    "email": "sekouamadougoita@cirim-mali.com",
    "adresse": "Bamako, Mali",
}


@app.route("/")
def accueil():
    """Page d'accueil du site."""
    return render_template("index.html", page_active="accueil", coord=COORDONNEES)


@app.route("/services/")
def services():
    """Page présentant les services proposés par CIRIM."""
    return render_template("services.html", page_active="services", coord=COORDONNEES)


@app.route("/a-propos/")
def a_propos():
    """Page de présentation de l'entreprise et de son fondateur."""
    return render_template("apropos.html", page_active="apropos", coord=COORDONNEES)


@app.route("/contact/")
def contact():
    """Page de contact : coordonnées uniquement, pas de formulaire."""
    return render_template("contact.html", page_active="contact", coord=COORDONNEES)


@app.route("/politique-de-confidentialite/")
def confidentialite():
    """Politique de confidentialité (mentions RGPD/loi malienne)."""
    return render_template("confidentialite.html", page_active="confidentialite", coord=COORDONNEES)


@app.route("/conditions-generales-utilisation/")
def cgu():
    """Conditions générales d'utilisation (avec mentions légales)."""
    return render_template("cgu.html", page_active="cgu", coord=COORDONNEES)


@app.route("/politique-de-cookies/")
def cookies():
    """Politique de cookies : le site n'en utilise aucun."""
    return render_template("cookies.html", page_active="cookies", coord=COORDONNEES)


# Ce bloc ne s'exécute que si on lance directement "python app.py"
# (et pas si le fichier est importé ailleurs).
if __name__ == "__main__":
    # debug=True affiche les erreurs détaillées et recharge le site
    # automatiquement à chaque modification du code pendant le développement.
    # Pensez à le mettre à False avant une mise en ligne définitive.
    app.run(debug=True)
