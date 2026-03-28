class bird:
    type = "bird"

    def __init__ (self, name, color):
        self.name = name
        self.color = color

blue = bird("Blue", "Blue")
woo = bird("Woo", "Rainbow")

print("The name of Blue is " + blue.name)
print("The type of Blue is " + blue.type)
print("The color of Blue is " + blue.color)

print("The name of Woo is " + woo.name)
print("The type of Woo is " + woo.type)
print("The color of Woo is " + woo.color)