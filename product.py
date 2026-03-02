class Product:
    """
    Represents a product entity.
    """

    def __init__(self, product_id: int, name: str, price: float, quantity: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return (
            f"ID: {self.product_id} | "
            f"Name: {self.name} | "
            f"Price: {self.price} | "
            f"Quantity: {self.quantity}"
        )