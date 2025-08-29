#class
class Device:
    def __init__(self, brand):
        self.brand = brand
    
    def show_brand(self):
        print(f"📌 Device brand: {self.brand}")

# Child class (Smartphone inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model):
        super().__init__(brand)   # inherit brand from Device
        self.model = model
    
    def call(self, name):
        print(f"📞 Calling {name} using {self.brand} {self.model}...")

    def text(self, name, message):
        print(f"💬 Sending '{message}' to {name} from {self.model}")

# Create objects
phone1 = Smartphone("Apple", "iPhone 14")
phone2 = Smartphone("Samsung", "Galaxy A55")

# Test methods
phone1.show_brand()
phone1.call("Alice")
phone2.text("Bob", "Hey! How are you?")
