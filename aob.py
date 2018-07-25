import random

class Ship(object): #all ship types inherit this class

    def __init__(self, name, length, cannon, mortar, deck,
                 speed , weight, armour, crew):
        self.name = name
        self.crew = crew
        self.length = length
        self.cannon = cannon
        self.mortar = mortar
        self.deck = deck
        self.speed = speed
        self.weight = weight
        self.armour = armour
        self.crew_health = crew_health

    def attack_cannon(self, other):
        if other.armour <= 0:
            other.armour = 0
            print(other.name + ' is Kaput!')
        else:
            cannon_damage = self.cannon*3*round(random.uniform(0.7,1),2) #number of cannon*damage per round*prob of hitting
            if cannon_damage >= other.armour:
                other.armour = 0
                print(other.name + ' is Kaput!')
            else:
                other.armour = other.armour - cannon_damage
                print(other.name + ' armour: ' + str(other.armour))

    def attack_mortar(self, other):
        if other.armour <= 0:
            other.armour = 0
            print(other.name + ' is Kaput!')
        else:
            mortar_damage = self.mortar*30*round(random.uniform(0.3,1),2) #number of cannon*damage per round*prob of hitting
            if mortar_damage >= other.armour:
                other.armour = 0
                print(other.name + ' is Kaput!')
            else:
                other.armour = other.armour - mortar_damage
                print(other.name + ' armour: ' + str(other.armour))


class Brig(Ship):

    def __init__(self, name):
        self.name = name
        self.length = 37.5
        self.cannon = 8                #on each side
        self.mortar = 1
        self.deck = 1
        self.speed = 3
        self.weight = 350
        self.armour = 100
        self.crew = 20
