# main.py
from product import Product
from product_manager import ProductManager

def main():
    manager = ProductManager()

    while True:
        print("\n=== Gestion des Produits ===")
        print("1. Ajouter un produit")
        print("2. Chercher un produit par ID")
        print("3. Mettre à jour un produit")
        print("4. Supprimer un produit")
        print("5. Lister tous les produits")
        print("6. Quitter")

        choice = input("Choisis une option de  (1-6) : ")

        if choice == "1":
            product_id = int(input("ID du produit : "))
            name = input("Nom : ")
            price = float(input("Prix : "))
            quantity = int(input("Quantité : "))
            product = Product(product_id, name, price, quantity)
            manager.add_product(product)

        elif choice == "2":
            product_id = int(input("ID du produit à chercher : "))
            product = manager.get_product(product_id)
            if product:
                print(product)

        elif choice == "3":
            product_id = int(input("ID du produit à modifier : "))
            name = input("Nouveau nom (laisser vide pour ne pas changer) : ")
            price_input = input("Nouveau prix (laisser vide pour ne pas changer) : ")
            quantity_input = input("Nouvelle quantité (laisser vide pour ne pas changer) : ")

            # Transforme en float/int si ce n'est pas vide
            price = float(price_input) if price_input else None
            quantity = int(quantity_input) if quantity_input else None
            name = name if name else None

            manager.update_product(product_id, name=name, price=price, quantity=quantity)

        elif choice == "4":
            product_id = int(input("ID du produit à supprimer : "))
            manager.delete_product(product_id)

        elif choice == "5":
            manager.list_products()

        elif choice == "6":
            print("Au revoir !")
            break

        else:
            print("Option invalide, réessaie.")

if __name__ == "__main__":
    main()