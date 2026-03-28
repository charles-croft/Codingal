choice = input("Enter 'rect' for Rectangle or 'sq' for Square: ").lower()

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        result = self.width * self.height
        print(f"Rectangle Area: {result}")

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def calculate_area(self):
        result = self.width * self.height
        print(f"Square Area: {result}")

if choice == 'rect':
    w = float(input("Enter width: "))
    h = float(input("Enter height: "))
    obj = Rectangle(w, h)
    obj.calculate_area()

elif choice == 'sq':
    s = float(input("Enter side: "))
    obj = Square(s)
    obj.calculate_area()

else:
    print("Invalid choice")