class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement move()")

class Car(Vehicle):
    def move(self):
        print("🚗 Driving")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying")

class Boat(Vehicle):
    def move(self):
        print("🚤 Sailing")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
