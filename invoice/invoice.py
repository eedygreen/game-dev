from item import Item
class Invoice:
    """Invoice for Customer"""
    def __init__(self, item: Item, quantity: int, discount: float = 0) -> None:
        self.item = item
        self.discount = discount
        self.quantity = quantity
        self._sub_total = (item.price * quantity) - discount

    def __repr__(self) -> str:
        return f"<class of 'Invoice'>"

    def __str__(self) -> str:
        return (
            f"Item: {self.item}, Discount: ${self.discount}, Quantity: {self.quantity}," 
            f" Sub_Total: ${self.get_sub_total():.2f}"
            )

    def get_sub_total(self) -> float:
        return self._sub_total