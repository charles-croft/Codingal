class bird:

    def __init__(self):
        print("Bird is ready")
    def swim(swim):
        print("Swim faster")
    def whoisthis(self):
        print("This is Bird")
    
class penguin(bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")

    def whoisthis(self):
        print("This is Penguin")

    def run(self):
        print("Run faster")

peggy = penguin()
peggy.whoisthis()
peggy.run()
peggy.swim()