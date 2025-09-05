warrior_name = "Thor"
warrior_health = 100
warrior_attack = 50

mage_name = "Gandalf"
mage_health = 80
mage_attack = 70

def attack_warrior():
    print(f'Warrior attacks wih power',warrior_attack)

def attack_mage():
    print(f'Mage attacks with the power',mage_attack)

attack_warrior()
attack_mage()


'''
Problem in this code :

1. Redundant Code
2. Hard to expand
3. No Structure
'''

'''
in OOP, object has two things - Attributes(Properties), Behaviour(Actions)
ex - car is an object with Attribute(Color=red) and Behaviour(run, stop).

instead of writing everything separately, we can group actions and data and convert it into object. Here OOP concepts came

in our example we stored all attributes in separate variables which results in code duplication, OOP solves this problem by writing all the attributes of a particular object altogether

in oop, we represent real world things as an object containing two things: data(properties/attributes), functions(methods/behaviour)  

OOP solves problems : code duplication, code complexity, objects interact with each other
'''