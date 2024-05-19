# parent class

class Item():
    def __init__(self, sku):
        self.sku = sku

    def print_sku(self):
        print("the  sku is {}".format(self.sku))

class Garment():
    def __init__(self, section,type):
        self.section = section
        self.type = type

    def print_type(self):
        print("the type is {},{}".format(self.section,self.type))

class Shirt(Item,Garment):
    def __init__(self,sku,section,type,name,color,price):
        self.name = name
        self.color = color
        self.price = price
        Garment.__init__(self,section,type)
        Item.__init__(self,sku)

    def print_shirt(self):
        print("the name is {}, the color is {}, the price is {}".format(self.name,self.color,self.price))

lol = Shirt("001","men","shirts","t-shirt","blue",200)

lol.print_shirt()
lol.print_type()
lol.print_sku()