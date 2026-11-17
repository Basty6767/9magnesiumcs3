# 1. What is duck typing, as explained in the video?
#      - Duck typing is another way to achieve polymorphism besides using inheritance. Objects can be treated as if they are a different typ as long as they have the minimum necessary attributes and methods. It follows the adage: "if it looks like a duck and qucks like a duck, it must be a duck."

# 2. What did the car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
#      - Because the for loop calls animal.speak() and prints animal.alive, the car class needed both the speak() method and the alive attribute.

class Car:
    def move(self):
        print("The car drives on the road.")
        
class Boat:
    def move(self):
        print("The boat sails on the water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")
        
def start_trip(vehicle):
    vehicle.move()

car = Car()
boat = Boat()
drone = Drone()

start_trip(car)
start_trip(boat)
start_trip(drone)   

# 3. How does the code in 2.2 demonstrate polymorphism?
#      - Even though car, boat, and drone do not inherit from a shared parent class, each class implements the minimum required move() method. Because they all share that method name, the single start_trip() function can treat all 3 objects interchangeably and trigger each vehicle's own version of move(), achieving polymorphism through duck typing.