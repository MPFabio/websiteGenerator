# Utilisation de l'image Python officielle en tant que base
FROM python:3.9-slim

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copie des fichiers nécessaires dans le conteneur
COPY . .

# Installation des dépendances Python définies dans le fichier requirements.txt
RUN pip install --no-cache-dir requests flask
