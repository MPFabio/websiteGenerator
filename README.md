Explication du fonctionnement des scripts

Les scripts websitegeneratorloopfor.py et websitegeneratorloopwhile.py sont conçus pour automatiser le processus de génération de sites Web statiques à partir de modèles HTML et de données JSON. Voici une explication générale de leur fonctionnement :

    Récupération des données JSON :
        Les scripts utilisent le module requests pour effectuer des requêtes HTTP vers une API distante qui fournit des données JSON sur les sites Web disponibles.
        Ils récupèrent les données sur les sites disponibles et sur les détails spécifiques des sites à partir des réponses JSON.

    Choix du site à générer :
        Une fois les données JSON récupérées, les scripts affichent une liste des sites disponibles à l'utilisateur.
        L'utilisateur est invité à choisir un site en saisissant le numéro correspondant.

    Génération du site statique :
        Après avoir reçu la sélection de l'utilisateur, les scripts créent un répertoire pour le site sélectionné dans le répertoire websites/.
        Ils copient un modèle HTML de page index dans ce répertoire et remplacent les balises de contenu dans le modèle HTML par les valeurs spécifiques du site, telles que le titre, les couleurs, le texte, et les chemins des images.
        Ils copient également les images correspondantes du répertoire assets/images/ dans le répertoire du site.

    Lancement de l'API Flask :
        Une fois que le site statique est généré, les scripts lancent un serveur API Flask à l'aide du script api.py.
        Cet API sert les fichiers statiques du site généré, permettant ainsi de visualiser le site dans un navigateur.

En résumé, ces scripts automatisent tout le processus de création d'un site Web statique en récupérant des données JSON, en les utilisant pour remplir un modèle HTML, en copiant les fichiers nécessaires, et en lançant un serveur pour servir le site généré.
