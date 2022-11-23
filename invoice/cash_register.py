from datetime import datetime
from customer import Customer
from invoice import Invoice
from item import Item
import json

class CashRegister:
    """Cash Register"""

    def __init__(self, customer: Customer) -> None:
        self.customer = customer
        self.items: dict[str, Invoice] = {}
        self.purchase_date = datetime.now()
        self._invoice_total = 0

    def __repr__(self) -> str:
        return f"<class of 'CashRegister'>"

    def __str__(self) -> str:
        return f"Customer: {self.customer}, Total Items: {len(self.items)}"

    def _increase_invoice_total(self, item: Invoice) -> None:
        """Increase Invoice Total"""
        self._invoice_total += item.get_sub_total()

    def _decrease_invoice_total(self, item: Invoice) -> None:
        """Decrease Invoice Total"""
        self._invoice_total -= item.get_sub_total()

    def add_item(self, item: Item, qty: int = 1, discount: float = 0) -> None:
        """Add Item to Invoice"""
        if item.name not in self.items:
            new_item = Invoice(item, qty, discount)
            self.items[item.name] = new_item
            self._increase_invoice_total(new_item)
        else:
            return f"{self.items[item.name]} already exists!"

    def update_item(self, item: Item, qty: int = 1, discount: float = 0) -> None:
        """Update an existin Item to Invoice"""
        if item.name in self.items:
            existing_item = self.items[item.name]
            self._decrease_invoice_total(existing_item)

            new_item = Invoice(item, qty, discount)
            self.items[item.name] = new_item
            self._increase_invoice_total(new_item)
        else:
            return f"{self.items[item.name]} not in Cart!"

    def remove_item(self, item: Item, qty: int = 1, discount: float = 0) -> None:
        """Remove an existing Item from Invoice"""
        if item.name in self.items:
            existing_item = self.items[item.name]
            self._decrease_invoice_total(existing_item)

            del self.items[item.name]

    def get_invoice_total(self) -> float:
        """Get Invoice Total"""
        return self._invoice_total

    def display_invoice(self) -> None:
        """Get Invoice Items"""
        print()
        print("+" * 50)
        print(self)
        print(f"Purchase Date: {self.purchase_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 50)
        for item in self.items.values():
            print(item)
        print("=" * 50)
        print(f"Total: ${self.get_invoice_total():.2f}")

    def get_items(self) -> dict:
        """Get Invoice Items"""
        dict_item = {}
        for item_name, invoice_item in self.items.items():
            dict_item[item_name] = invoice_item.dict()
        return dict_item

    def checkout(self) -> dict:
        """Checkout Invoice"""
        cash_register = {
            "customer": self.customer.dict(),
            "items": self.get_items(),
            "purchase_date": self.purchase_date.strftime("%Y-%m-%d %H:%M:%S"),
            "invoice_total": self.get_invoice_total(),
        }

        return cash_register

    def json_file(self) -> str:
        """Get JSON File"""
        return json.dumps(self.checkout(), indent=4, sort_keys=True)