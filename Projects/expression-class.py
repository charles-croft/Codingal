class Expression:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def calculate_addition(self):
        result = self.num1 + self.num2 + self.num3
        print(f"The sum of the three numbers is {result}")

obj = Expression(
    int(input("Enter first number: ")), 
    int(input("Enter second number: ")), 
    int(input("Enter third number: "))
)

obj.calculate_addition()