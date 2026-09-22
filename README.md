# Site vitrine CIRIM

Site vitrine en Flask pour **CIRIM** (Conseil en Ingénierie Risques Industriels
et Maintenance), l'entreprise individuelle de Sekou Amadou GOITA.

4 pages : Accueil, Services, À propos, Contact. La page Contact affiche
uniquement les coordonnées (téléphone, WhatsApp, e-mail, adresse) : il n'y a
ni formulaire, ni base de données.

## Structure du projet

```
Site Entreprise/
├── app.py                 → lance le site et définit les 4 pages (routes)
├── requirements.txt       → liste des dépendances Python à installer
├── .gitignore              → fichiers à ne pas mettre sur Git
├── templates/              → pages HTML (remplies par Flask)
│   ├── base.html            → menu + pied de page communs à toutes les pages
│   ├── index.html           → page Accueil
│   ├── services.html        → page Services
│   ├── apropos.html         → page À propos
│   └── contact.html         → page Contact
└── static/
    ├── css/
    │   └── style.css        → toute la mise en forme et l'adaptation mobile
    └── img/
        ├── logo.png          → logo CIRIM (menu du site)
        ├── logo-icone.png     → pictogramme seul du logo
        ├── favicon.png        → icône affichée dans l'onglet du navigateur
        └── fondateur-*.jpg    → photos du fondateur (page À propos)
```

## Lancer le site en local

Il faut avoir Python installé (version 3.9 ou plus récente).

1. **Ouvrir un terminal dans le dossier du projet** (`Site Entreprise/`).

2. **Créer un environnement virtuel** (un dossier isolé pour les dépendances
   du projet, pour ne pas mélanger avec d'autres projets Python) :

   ```bash
   python3 -m venv .venv
   ```

3. **Activer l'environnement virtuel :**

   - Sur Mac / Linux :
     ```bash
     source .venv/bin/activate
     ```
   - Sur Windows :
     ```bash
     .venv\Scripts\activate
     ```

   Une fois activé, vous devez voir `(.venv)` apparaître au début de la ligne
   de commande.

4. **Installer Flask** (la seule dépendance du projet) :

   ```bash
   pip install -r requirements.txt
   ```

5. **Lancer le site :**

   ```bash
   python app.py
   ```

6. **Ouvrir le site dans un navigateur** à l'adresse indiquée dans le
   terminal, généralement :

   ```
   http://127.0.0.1:5000
   ```

Pour arrêter le site, retournez dans le terminal et appuyez sur `Ctrl + C`.

## Modifier les textes du site

Vous n'avez pas besoin de savoir programmer pour changer les textes : il
suffit de modifier le bon fichier avec un éditeur de texte (par exemple
Bloc-notes, TextEdit, VS Code...) et d'enregistrer.

- **Coordonnées** (téléphone, WhatsApp, e-mail, adresse) : tout se trouve au
  même endroit, en haut du fichier `app.py`, dans le dictionnaire
  `COORDONNEES`. Modifiez la valeur entre guillemets après les deux-points,
  par exemple :

  ```python
  "telephone": "07 65 73 63 64",
  ```

  Ces coordonnées sont ensuite utilisées automatiquement sur toutes les
  pages (menu, pied de page, page Contact) : pas besoin de les changer
  ailleurs.

- **Textes de la page d'accueil** : fichier `templates/index.html`.
- **Liste et description des services** : fichier `templates/services.html`.
- **Texte de présentation de l'entreprise** : fichier `templates/apropos.html`.
- **Page Contact** : fichier `templates/contact.html` (les coordonnées
  elles-mêmes viennent de `app.py`, voir ci-dessus).

Le texte à modifier se trouve toujours entre les balises HTML, par exemple
dans `<p>...</p>` ou `<h1>...</h1>` : vous pouvez changer le texte à
l'intérieur sans toucher au reste.

## Remplacer une photo

1. Placez votre nouvelle image dans `static/img/`.
2. Dans le fichier HTML concerné (`templates/apropos.html` pour les photos
   du fondateur), remplacez le nom de fichier dans la balise `<img src="...">`
   par le nom de votre nouvelle image.

Pour de meilleures performances, préférez des photos qui ne dépassent pas
environ 1100 pixels de large (les photos de téléphone sont souvent bien plus
grandes que nécessaire pour un site web).

## Modifier les couleurs et la mise en forme

Tout est centralisé dans `static/css/style.css`. Les deux couleurs
principales du site sont définies tout en haut du fichier et peuvent être
changées facilement :

```css
--couleur-principale: #0b2545;   /* bleu marine */
--couleur-accent: #e2711d;       /* orange */
```

## Mettre le site en ligne (gratuitement, avec GitHub Pages)

Le site n'ayant ni formulaire ni base de données, il est converti en pages
HTML statiques puis hébergé gratuitement sur GitHub Pages.

- `freeze.py` génère le site statique dans le dossier `build/` (avec
  [Frozen-Flask](https://frozen-flask.readthedocs.io/)). Pour tester en
  local :

  ```bash
  python freeze.py
  cd build && python -m http.server 8000
  ```

  Le site s'affiche alors sur `http://127.0.0.1:8000`.

- À chaque `git push` sur `main`, le workflow GitHub Actions
  `.github/workflows/deploy.yml` régénère automatiquement le site et le
  publie sur GitHub Pages : pas besoin de lancer `freeze.py` à la main avant
  de pousser.

- Pour activer GitHub Pages (une seule fois) : sur GitHub, aller dans
  **Settings → Pages**, et choisir **Source : GitHub Actions**.

- Pour connecter un nom de domaine personnalisé : ajouter un fichier
  `CNAME` à la racine du projet contenant le nom de domaine (ex.
  `cirim-conseil.com`), configurer les enregistrements DNS chez le
  registrar du domaine, puis renseigner le domaine dans **Settings → Pages
  → Custom domain**.
