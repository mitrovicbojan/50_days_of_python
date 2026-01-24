'''
Build a Game Character Stats Tracker

Create a class named GameCharacter that represents a game 
character and manages character stats.

When instantiated, a new GameCharacter object should 
have the following attributes:

_name set to the string given at the moment of the instantiation.
_health set to 100.
_mana set to 50.
_level set to 1.
Create a name property for read-only access to the character's name.

For the health property:

Define a getter that returns the current health.
Define a setter that prevents health from being 
set below 0, and caps the health at 100.
For the mana property:

Define a getter that returns the current mana.
Define a setter that prevents mana from being set below 0, and caps the mana at 50.
Create a getter for level to return the character's current level.

Define a method named level_up that:

Increases the character's level by 1.
Resets health to 100 and mana to 50 using their corresponding property setters.
Prints a message in the form of <name> leveled up 
to <level>! (where <name> and <level> should be replaced by the 
character's name and new level, respectively).
Define a __str__ method that returns a formatted string including:

The character's name.
The character's level.
The character's current health.
The character's current mana.
'''

class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1
        
    def __str__(self):
        return f'Name: {self._name}\nLevel: {self._level}\nHealth: {self._health}\nMana: {self._mana}'
    
    @property
    def name(self):
        return self._name
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, new_health):
        self._health = new_health 
        
        if new_health in range(0,100):
            self._health = new_health
             
        if new_health < 0:
            self._health = 0
        if new_health > 100:
            self._health = 100             
            
        return self._health
    
    
    @property
    def mana(self):
        return self._mana
    
    @mana.setter
    def mana(self, new_mana):
        self._mana = new_mana 
        
        if new_mana in range(0,50):
            self._mana = new_mana
             
        if new_mana < 0:
            self._mana = 0
        if new_mana > 50:
            self._mana = 50             
            
        return self._mana
    
    @property
    def level(self):
        return self._level
    
    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self.level}!")
    
hero = GameCharacter("Kratos")
print(hero)
hero.health = 1
print(hero.health)
print(hero)
hero.level_up()
print(hero)