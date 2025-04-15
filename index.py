# How to create a class using in Object oriented programming 
# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(Raphael):
        return f"I am {Raphael.name} from {Raphael.origin}, and I use {Raphael.power}!"

    def use_power(Raphael):
        return f"{Raphael.name} uses {Raphael.power} to save the day!"

# Subclass using inheritance
class TechHero(Superhero):
    def __init__(self, name, power, origin, gadget):
        super().__init__(name, power, origin)
        self.gadget = gadget

    def use_power(self):
        # Polymorphism in action (overriding the parent method)
        return f"{self.name} uses {self.gadget} to hack into the system and stop the villains!"

# Create objects
hero1 = Superhero("Aquamind", "Telepathy", "Atlantis")
hero2 = TechHero("ByteBlaster", "Technomancy", "Silicon City", "CyberGlove")

# Output
print(hero1.introduce())
print(hero1.use_power())
print(hero2.introduce())
print(hero2.use_power())
#How tocarry out POLYMORPHISm
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# How to Enact Polymorphism

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
