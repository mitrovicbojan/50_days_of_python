# Assignment 1:

"""
Define a class hierarchy representing animals with a parent class Animal
and child classes such as dog, fish and bird. Each subclass animal should have
a name and an age and should have 2 methods defined in it: move(), eat().
The move method needs to be specific for a given animal where as the
eat() method should be generic for all animals. The methods don't need to
do anything except print information about who is doing what.

After creating the class hierarchy, create instances of each of the 3 animals
dog, fish and bird and make them eat and move.

"""
# Your Code Below:

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def move(self):
        print("This animal is moving")
    def eat(self):
        print("This animal eats")

class Dog(Animal):
    def move(self):
        print("Dog moves on 4 legs")
    def eat(self):
        print("Dog eat dog")
    
class Fish(Animal):
    def move(self):
        print("Fish swims")
        
    def eat(self):
        print("Fish eat fish")
        
class Bird(Animal):
    def move(self):
        print("Bird is flying")
        
    def eat(self):
        print("Fish eat fish")
        

dog = Dog("Buddy", 2)
fish = Fish("Nemo", 3)
bird = Bird("Tweety", 5)

dog.eat()
dog.move()
fish.eat()
fish.move()
bird.eat()
bird.move()

