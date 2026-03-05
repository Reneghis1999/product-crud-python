# product_manager.py
from product import Product
from database import SessionLocal, Base, engine

# Créer la table dans SQLite si elle n'existe pas
Base.metadata.create_all(bind=engine)

class ProductManager:
    def __init__(self):
        self.session = SessionLocal()  # La session pour interagir avec la base

    def add_product(self, id, name, price, quantity):
        product = Product(id=id, name=name, price=price, quantity=quantity)
        self.session.add(product)
        self.session.commit()
        print(f"Produit ajouté : {product}")

    def get_product(self, id):
        return self.session.query(Product).filter(Product.id == id).first()

    def update_product(self, id, name=None, price=None, quantity=None):
        product = self.get_product(id)
        if not product:
            print("Produit non trouvé")
            return
        if name: product.name = name
        if price: product.price = price
        if quantity: product.quantity = quantity
        self.session.commit()
        print(f"Produit mis à jour : {product}")

    def delete_product(self, id):
        product = self.get_product(id)
        if not product:
            print("Produit non trouvé")
            return
        self.session.delete(product)
        self.session.commit()
        print(f"Produit supprimé : {product}")

    def list_products(self):
        products = self.session.query(Product).all()
        if not products:
            print("Aucun produit dans le stock")
        for p in products:
            print(p)