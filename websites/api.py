import os  # Importation du module os pour accéder aux fonctionnalités liées au système d'exploitation
import sys  # Importation du module sys pour accéder aux arguments de la ligne de commande
from flask import Flask, send_from_directory  # Importation de la classe Flask pour créer une application web Flask et de la fonction send_from_directory pour envoyer des fichiers statiques

app = Flask(__name__)  # Création d'une instance de l'application Flask

@app.route('/')  # Définition de la route pour l'URL '/'
def index():
    # Récupère le nom du répertoire du site à partir des arguments passés à l'API
    selected_website_name = os.path.basename(os.path.normpath(sys.argv[1])).replace(".", "_")
    # Construit le chemin vers le fichier index.html du site sélectionné
    index_path = os.path.join(selected_website_name.replace(".", "_"), "index.html")
    # Lit le contenu du fichier index.html
    with open(index_path, "r") as file:
        index_content = file.read()
    return index_content  # Renvoie le contenu du fichier index.html

# Route pour servir les fichiers statiques
@app.route('/<path:filename>')
def serve_static(filename):
    # Récupère le nom du répertoire du site à partir des arguments passés à l'API
    selected_website_name = os.path.basename(os.path.normpath(sys.argv[1])).replace(".", "_")
    # Construit le chemin vers le répertoire des fichiers statiques du site sélectionné
    static_dir = os.path.join(selected_website_name.replace(".", "_"))
    # Envoie le fichier statique demandé depuis le répertoire des fichiers statiques
    return send_from_directory(static_dir, filename)

if __name__ == '__main__':
    # Vérifie si un port est spécifié en tant qu'argument en ligne de commande
    if len(sys.argv) > 2:
        port = int(sys.argv[2])  # Utilise le deuxième argument en tant que numéro de port
    else:
        port = 5000  # Port par défaut

    app.run(debug=True, host="0.0.0.0", port=port)  # Lancement de l'application Flask en spécifiant le port