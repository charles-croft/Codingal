class Dog:
    animal = "Dog"

    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

chica = Dog("Havanese", "White with Tan Spots")
mya = Dog("Havanese", "Black")

print(f"Chica: {chica.animal}, Breed: {chica.breed}, Colour: {chica.colour}")
print(f"Mya: {mya.animal}, Breed: {mya.breed}, Colour: {mya.colour}")