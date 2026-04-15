class Computer:
    def __init__(self):
        self.__maxprice = 1499.99
    def sell(self):
        print("Selling price is {}".format(self.__maxprice))
    def setmaxprice(self, price):
        self.__maxprice = price

laptop = Computer()
laptop.sell()
# laptop.__maxprice(1999.99)
# laptop.sell()
laptop.setmaxprice(1999.99)
laptop.sell()