class Character:
    def __init__(self, name, health, attack, weakness):
        self.name = name
        self.health = health
        self.attack = attack
        self.weakness = weakness

    def attack_enemy(self):
        print(f'{self.name} attacks with power {self.attack} having weakness {self.weakness}')

warrior = Character("Thor", 100, 50, "Speed")
mage = Character("Gandalf", 80, 70, "Magic")
archer = Character("Archer", 80, 90, "Darkness")

warrior.attack_enemy()
mage.attack_enemy()
archer.attack_enemy()

'''
Here, we'd wrote main logic once and then creating its objects by calling our class.
Doing this our code is scalable and organized.
Now we can add multiple characters
the properties and actions matches with real life which helps programming easier

OOP is best for large projects as :
it enhances code reusability
better organization 
security
easier maintenance
'''

"""
OOP groups data and behaviour into objects helping in reusability, readability, scalability 
"""