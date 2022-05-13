# Parent Class 1
class Item():
    def __init__(self, sku):
        self.sku = sku

    def print_sku(self):
        print("The sku is {}".format(self.sku))

# Parent Class 2
class Garment():
    def __init__(self, section, type):
        self.section = section
        self.type = type
    def print_garment(self):
        print("The garment is in {}, {}".format(self.section, self.type))

# Child Class
class Shirts(Item, Garment):
    def __init__(self, sku, section, type, name, color):
        self.name = name
        self.color = color
        Item.__init__(self,sku)
        Garment.__init__(self,section,type)

    def print_shirt(self):
        print("{} {} is on sale".format(self.color, self.name))

Blouse = Shirts("0001", 43, "Tops", "Formal Blouse", "White")
Blouse.print_sku()
Blouse.print_garment()
Blouse.print_shirt()
