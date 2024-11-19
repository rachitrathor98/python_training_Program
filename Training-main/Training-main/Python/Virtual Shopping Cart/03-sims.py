
class Items:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def displayItems(self):
        print(f'''Name: {self.name}
Price: {self.price}
Quantity: {self.quantity}''')

class Inventery:
    def __init__(self):
        self.items = []  

    def additems(self, name, price, quantity):
        self.items.append(Items(name, price, quantity))

    def displayItems(self):
        for item in self.items:
            item.displayItems()
            print()  

Inventery1 = Inventery()
Inventery2 = Inventery()


Inventery1.additems('Pen', 150, 2500)
Inventery1.additems('Pencil', 150, 2500)
Inventery1.additems('Box', 150, 2500)
Inventery1.additems('Scale', 150, 2500)
''''
class variable : to create a value accesible to whole class should be diffrent aporoach
MRO : method Resoluction Order 
Q-  be write written statement in constructor


'''

Inventery1.displayItems()