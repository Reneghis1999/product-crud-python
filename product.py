# product.py
from sqlalchemy import Column, Integer, String, Float
from database import Base

class Product(Base):
    """
    Represents a product entity, stored in SQLite via SQLAlchemy ORM.
    """
    __tablename__ = "products"

    # Colonnes
    id = Column(Integer, primary_key=True, index=True)   # ID du produit
    name = Column(String, nullable=False)               # Nom
    price = Column(Float, nullable=False)              # Prix
    quantity = Column(Integer, nullable=False)         # Quantité

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price}, quantity={self.quantity})"