from flask import Flask

import os

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


app = Flask(__name__)

# Récupérer les informations de connexion à partir des variables d'environnement
database = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")

# Connectez-vous à PostgreSQL
conn = psycopg2.connect(
    dbname=database,
    user=user,
    password=password,
    host=host,
    port=port
)

# Créez une nouvelle base de données
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()
cursor.execute("CREATE DATABASE test;")
cursor.close()
conn.close()

# Connectez-vous à la nouvelle base de données
conn = psycopg2.connect(
    dbname="test",
    user=user,
    password=password,
    host=host,
    port=port
)

# Créez une nouvelle table
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE insee_dept (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    );
""")
conn.commit()
cursor.close()
conn.close()


@app.route('/')
def hello_world():
    return 'Bonjour, monde!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')