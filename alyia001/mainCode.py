#File: mainCode.py
#Description: Main Code for the implementation of a common RPG uml design
#Author: Ian Amir Al Faily
#StudentID:110416702
#EmailID: Alyia001
#This is my own work as defined by the University's Academic Misconduct Policy.






class Alchemist:
    def __init__(self, attack, strength, defense, magic, range, necromancy):
        self.attack = attack
        self.strength = strength
        self.defense = defense
        self.magic = magic
        self.range = range
        self.necromancy = necromancy

    def mix_potion(self, ingredient1, ingredient2):
        pass

    def drink_potion(self, potion):
        pass

    def collect_reagent(self, reagent):
        pass

    def refine_reagents(self):
        pass


class Laboratory:
    def __init__(self):
        self.potions = []
        self.herbs = []
        self.catalysts = []

    def mix_potion(self, ingredient1, ingredient2):
        pass

    def add_reagent(self, reagent):
        pass

    def refine_reagents(self):
        pass


class Potion:
    def __init__(self, name, stat_attribute, boost_attribute):
        self.name = name
        self.stat_attribute = stat_attribute
        self.boost_attribute = boost_attribute

    def calculate_boost(self):
        pass

class Reagent:
    def __init__(self, name, potency):
        self.name = name
        self.potency = potency

    def refine(self):
        pass
