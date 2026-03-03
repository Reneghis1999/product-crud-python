# product_manager.py
from product import Product

class ProductManager:
    def __init__(self):
        # La liste qui contiendra tous nos produits
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)
        print(f"Produit ajouté : {product.name} (ID {product.product_id})")

    def get_product(self, product_id: int):
        # Chercher un produit par son ID
        for product in self.products:
            if product.product_id == product_id:
                return product
        
        print(f"Aucun produit trouvé avec l'ID {product_id}")
        return None

    def update_product(self, product_id: int, name=None, price=None, quantity=None):
        product = self.get_product(product_id)
        if product:
            if name is not None:
                product.name = name
            if price is not None:
                product.price = price
            if quantity is not None:
                product.quantity = quantity
            print(f"Produit mis à jour : {product}")
        else:
            print(f"Impossible de mettre à jour : produit {product_id} introuvable")

    def delete_product(self, product_id: int):
        product = self.get_product(product_id)
        if product:
            self.products.remove(product)
            print(f"Produit supprimé : {product}")
        else:
            print(f"Impossible de supprimer : produit {product_id} introuvable")

    def list_products(self):
        # Affiche tous les produits
        if not self.products:
            print("Aucun produit dans le stock")
        for product in self.products:
            print(product)