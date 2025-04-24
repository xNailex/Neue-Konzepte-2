class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.make} {self.model} Engine started")
    def stop(self):
        print(f"{self.make} {self.model} Engine stopped")
    def display_details(self):
        print(f"{self.year} {self.make} {self.model}")
    
car1 = Car("Seat", "Ibiza", 2017)
car1.display_details()
car1.start()
car1.stop()