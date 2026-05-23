class car:
    def fuel_type(self):
        pass
class bmw(car):
    def fuel_type(self):
        print("Diesel")
    def max_speed(self):
        print("305 km/h")
class ferrari(car):
    def fuel_type(self):
        print("Unleaded 98")
    def max_speed(self):
        print("350 km/h")
M5 = bmw()
F80 = ferrari()
M5.fuel_type()
M5.max_speed()
F80.fuel_type()
F80.max_speed()