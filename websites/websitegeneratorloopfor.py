import os  # Importation du module os pour manipuler les chemins de fichiers et les répertoires
import re  # Importation du module re pour utiliser les expressions régulières
import requests  # Importation du module requests pour effectuer des requêtes HTTP
import shutil  # Importation du module shutil pour effectuer des opérations de copie de fichiers
import subprocess # Importation du module subprocess pour exécuter des commandes système et des scripts externes

# Définition de la fonction principale du script
def main():
    # Effectue une requête GET vers l'URL spécifiée pour récupérer des données JSON sur les sites disponibles
    response_websites = requests.get("https://my-json-server.typicode.com/tiko69/jsonserver/websites")
    # Effectue une requête GET vers l'URL spécifiée pour récupérer des données JSON sur les détails spécifiques des sites
    response_website = requests.get("https://my-json-server.typicode.com/tiko69/jsonserver/website")
    
    # Vérifie si les requêtes ont réussi (statut code 200)
    if response_websites.status_code == 200 and response_website.status_code == 200:
        # Analyse les données JSON récupérées sur les sites disponibles
        websites_data = response_websites.json()
        # Analyse les données JSON récupérées sur les détails spécifiques des sites
        website_data = response_website.json()
        
        # Affiche un message invitant l'utilisateur à choisir un site parmi ceux disponibles
        print("Choisissez l'un des sites suivants :")
        
        # Boucle à travers les sites et les affiche avec leur numéro d'index
        for idx, website in enumerate(websites_data, 1):
            print(f"{idx} {website['website']} \n") 

        # Demande à l'utilisateur de saisir le numéro du site qu'il souhaite
        choice = input("Entrez le numéro du site que vous souhaitez : ")
        
        # Vérifie si la saisie est un nombre 
        if choice.isdigit():
            choice_int = int(choice)
            # Vérifie si la saisie est un nombre valide et se trouve dans la plage des indices des sites disponibles
            if 0 < choice_int <= len(websites_data):
                # Récupère le nom de domaine du site sélectionné
                selected_website_name = websites_data[choice_int - 1]['website']
                print(f"Nom de domaine sélectionné: {selected_website_name}")
                
                # Utilisation de la fonction next pour obtenir le prochain élément correspondant à notre critère de recherche.
                # qui parcourt tous les éléments de website_data, filtrés par un critère défini.
                website_info = next(site for site in website_data if site['title'].startswith(selected_website_name.split('.')[0]))

                # Remplace les points par des tirets bas dans le nom du site afin d'obtenir un nom de dossier valide lors du os.makedirs
                directory_path = os.path.join(selected_website_name.replace(".", "_"))
                os.makedirs(directory_path, exist_ok=True)
                
                # Chemin du fichier source à copier
                source_file = os.path.join("../templates/index.html")
                # Chemin du fichier de destination
                destination_file = os.path.join(directory_path, "index.html")
                
                # Vérifie si le fichier source existe
                if os.path.exists(source_file):
                    # Lecture du contenu du fichier source
                    with open(source_file, "r") as file:
                        html_content = file.read()
                    
                    # Remplace tous les occurrences dans html_content par la valeur correspondante de dans website_info.
                    # Si la valeur n'existe pas dans website_info, la chaîne vide est utilisée comme valeur par défaut.
                    html_content = re.sub(r"\[title\]", website_info.get('title', ''), html_content)
                    html_content = re.sub(r"\[body\.color\]", website_info.get('body', {}).get('color', ''), html_content)
                    html_content = re.sub(r"\[h1\.background-color\]", website_info.get('h1', {}).get('background-color', ''), html_content)
                    html_content = re.sub(r"\[h1\.color\]", website_info.get('h1', {}).get('color', ''), html_content)
                    html_content = re.sub(r"\[p\.color\]", website_info.get('p', {}).get('color', ''), html_content)
                    html_content = re.sub(r"\[h1\.text\]", website_info.get('h1', {}).get('text', ''), html_content)
                    html_content = re.sub(r"\[p\.text\]", website_info.get('p', {}).get('text', ''), html_content)
                    html_content = re.sub(r"\[img\.src\]", website_info.get('img', {}).get('src', ''), html_content)
                    html_content = re.sub(r"\[img\.alt\]", website_info.get('img', {}).get('alt', ''), html_content)

                    # Écriture du contenu modifié dans le fichier de destination
                    with open(destination_file, "w") as dest_file:
                        dest_file.write(html_content)
                    
                    print("Fichier index.html copié avec succès.")
                    
                    # Copie de l'image .webp si elle existe
                    image_source_path = os.path.join("../assets", website_info.get('img', {}).get('src', ''))
                    if os.path.exists(image_source_path):
                        # Obtenez le nom d'origine de l'image
                        image_name = os.path.basename(image_source_path)
                        # Construire le chemin de destination pour l'image en utilisant le nom d'origine
                        image_destination_path = os.path.join(directory_path, image_name)
                        # Copier l'image
                        shutil.copy(image_source_path, image_destination_path)
                        print("Image webp copiée avec succès.")

                    else:
                        print("L'image webp n'a pas été trouvée.")

                    # Lancement de l'API Flask depuis le script
                    api_script_path = os.path.join(directory_path, "../api.py")
                    subprocess.Popen(["python", api_script_path, selected_website_name])

                else:
                    print("Le fichier source n'existe pas.")
                    
            else:
                print("Choix invalide")
        else:
            print("Entrée invalide")
    else:
        print("Erreur lors de la récupération des données")

# Point d'entrée du script
if __name__ == "__main__":
    main()