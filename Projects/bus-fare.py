class Vehicle:
    def __init__(self, seating_capacity):
        self.subfee = seating_capacity * 100
        self.extra_fee = self.subfee / 10
        self.inrfee = self.subfee + self.extra_fee
        self.fee = self.inrfee * 0.015

class Bus(Vehicle):
    def __init__(self):
        super().__init__(50)
        self.seating_capacity = 50

BCI_Cruiser_13 = Bus()

print(f"Rupee fee: {BCI_Cruiser_13.inrfee} INR")
print(f"Australian fee: {BCI_Cruiser_13.fee} AUD")