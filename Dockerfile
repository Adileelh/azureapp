# Utiliser une image de base Python 3.8
FROM python:3.8-slim-buster

# Définir le répertoire de travail dans le conteneur Docker
WORKDIR /app

# Copier les fichiers de dépendances dans le conteneur
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source dans le conteneur
COPY . .

# Exposer le port sur lequel l'application s'exécute
EXPOSE 5000

# Lancer l'application
CMD [ "python", "app.py" ]