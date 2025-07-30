# Parent class
class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def start_engine(self):
        print(f"{self.brand}'s engine has started.")

    def info(self):
        print(f"Brand: {self.brand}, Wheels: {self.wheels}")


# Child class
class Car(Vehicle):
    def __init__(self, brand, model):
        # Inherit from Vehicle, assume cars have 4 wheels
        super().__init__(brand, wheels=4)
        self.model = model

    def play_music(self):
        print(f"Playing music in the {self.brand} {self.model}.")

    def info(self):
        super().info()
        print(f"Model: {self.model}")


# Usage
v = Vehicle("Yamaha", 2)
v.start_engine()
v.info()

print()

c = Car("Toyota", "Corolla")
c.start_engine()  # Inherited
c.info()          # Overridden and extended
c.play_music()    # Child-specific method
