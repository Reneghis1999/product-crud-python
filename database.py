# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Définir la base de données

# SQLite sera stockée dans un fichier "products.db"
DATABASE_URL = "sqlite:///products.db"

#  Créer l’engine SQLAlchemy

# L'engine est comme le moteur qui connecte Python à SQLite
engine = create_engine(
    DATABASE_URL,
    echo=True  # Affiche toutes les requêtes SQL dans la console (utile pour debug)
)


#  Créer une session

# La session permet de parler à la base : ajouter, lire, modifier, supprimer
SessionLocal = sessionmaker(bind=engine)


#  Base pour les modèles

# Tous les modèles SQLAlchemy (comme Product) doivent hériter de Base
Base = declarative_base()