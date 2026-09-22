# freeze.py
# ------------------------------------------------------------
# Convertit le site Flask en un dossier de fichiers HTML/CSS/images
# 100% statiques, prêts à être hébergés gratuitement (GitHub Pages,
# Cloudflare Pages...) sans avoir besoin de faire tourner un serveur
# Python en permanence.
#
# Utilisation :
#   python freeze.py
#
# Le résultat est généré dans le dossier build/. Ce dossier est
# régénéré automatiquement par GitHub Actions à chaque mise en ligne
# (voir .github/workflows/deploy.yml) : pas besoin de le lancer à la
# main sauf pour tester en local avant de pousser sur GitHub.
# ------------------------------------------------------------

from flask_frozen import Freezer

from app import app

app.config["FREEZER_DESTINATION"] = "build"
# Liens en chemins absolus (ex. "/a-propos/") : corrects tant que le site
# est servi à la racine d'un domaine (ce qui sera le cas avec le nom de
# domaine personnalisé). Donne des URLs propres, sans "/index.html" visible.
app.config["FREEZER_RELATIVE_URLS"] = False

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()
    print("Site statique généré dans le dossier build/")
