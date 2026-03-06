# product_manager.py
from product import Product
from database import SessionLocal, Base, engine

# Créer la table dans SQLite si elle n'existe pas
Base.metadata.create_all(bind=engine)

class ProductManager:
    def add_product(self, id, name, price, quantity):
        try:
            with SessionLocal() as session:
                product = Product(id=id, name=name, price=price, quantity=quantity)
                session.add(product)
                session.commit()
                print(f"Produit ajouté : {product}")
        except Exception as e:
            print(f"Erreur lors de l'ajout du produit : {e}")

    def get_product(self, id):
        try:
            with SessionLocal() as session:
                return session.query(Product).filter(Product.id == id).first()
        except Exception as e:
            print(f"Erreur lors de la récupération du produit : {e}")
            return None

    def update_product(self, id, name=None, price=None, quantity=None):
        try:
            with SessionLocal() as session:
                product = session.query(Product).filter(Product.id == id).first()
                if not product:
                    print("Produit non trouvé")
                    return
                if name: product.name = name
                if price: product.price = price
                if quantity: product.quantity = quantity
                session.commit()
                print(f"Produit mis à jour : {product}")
        except Exception as e:
            print(f"Erreur lors de la mise à jour du produit : {e}")

    def delete_product(self, id):
        try:
            with SessionLocal() as session:
                product = session.query(Product).filter(Product.id == id).first()
                if not product:
                    print("Produit non trouvé")
                    return
                session.delete(product)
                session.commit()
                print(f"Produit supprimé : {product}")
        except Exception as e:
            print(f"Erreur lors de la suppression du produit : {e}")

    def list_products(self):
        try:
            with SessionLocal() as session:
                products = session.query(Product).all()
                if not products:
                    print("Aucun produit dans le stock")
                for p in products:
                    print(p)
        except Exception as e:
            print(f"Erreur lors de la récupération des produits : {e}")