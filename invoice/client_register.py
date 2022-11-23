from cash_register import CashRegister
from customer import Customer
from item import Item


meat = Item(101, "Beef", 10.00, 3, "kg")
eggs = Item(102, "Eggs", 2.00, 12, "pcs")
rice = Item(103, "Rice", 5.00, 1, "kg")
beans = Item(104, "Beans", 3.00, 1, "kg")

cusomer_1 = Customer("John", "Doe")

register = CashRegister(cusomer_1)
register.add_item(meat, 2, 0.5)
register.add_item(eggs, 1, 0.5)
register.add_item(rice, 1, 0.5)
register.add_item(beans, 1, 0.5)
register.update_item(meat, 3, 1)

register.display_invoice()
print(register)

register.remove_item(meat, 1, 0.5)
register.display_invoice()
print(register)