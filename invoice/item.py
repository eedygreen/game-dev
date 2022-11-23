class Item:
    """Item for Catalog"""
    def __init__(self, id: int, name: str, price: float, quantity: int, measurement_unit: str) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.measurement_unit = measurement_unit

    def __repr__(self) -> str:
        return f"<class of 'Item'>"

    def __str__(self) -> str:
        return f"{self.id}, {self.name}, ${self.price}, {self.quantity}, {self.measurement_unit}"