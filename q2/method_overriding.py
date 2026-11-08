class Animal:
    def __init__(self, name: str):
        self._name = name
        
    def make_sound(self):
        pass
    
    def eat(self):
        pass
    
    def feed(self):
        return self.eat()
    

class Lion(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        
    def make_sound(self):
        return f"{self._name} roars loudly!"
    
    def eat(self):
        return f"{self._name} eats fresh meat."
    
class Elephant(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        
    def make_sound(self):
        return f"{self._name} trumpets!"
    
    def eat(self):
        return f"{self._name} eats grass and fruits."
    
class Monkey(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        
    def make_sound(self):
        return f"{self._name} chatters!"
    
    def eat(self):
        return f"{self._name} eats bananas."
    

lion = Lion("Simba")

elephant = Elephant("Dumbo")

monkey = Monkey("George")

print(lion.make_sound())
print(lion.feed())
print("-----")

print(elephant.make_sound())
print(elephant.feed())
print("-----")

print(monkey.make_sound())
print(monkey.feed())
print("-----")