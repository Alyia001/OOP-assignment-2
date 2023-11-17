#File: mainCode.py
#Description: Main Code for the implementation of a common RPG uml design
#Author: Ian Amir Al Faily
#StudentID:110416702
#EmailID: Alyia001
#This is my own work as defined by the University's Academic Misconduct Policy.






class Alchemist:
    def __init__(self):
        self.attack = 0
        self.strength = 0
        self.defence = 0
        self.magic = 0
        self.ranging = 0
        self.necromancy = 0

    def mix_potion(self, laboratory, ingredient1, ingredient2):
        potion = laboratory.mix_potion(ingredient1, ingredient2)
        if potion:
            self.drink_potion(potion)

    def drink_potion(self, potion):
        setattr(self, potion.stat_attribute, getattr(self, potion.stat_attribute) + potion.calculate_boost())

    def collect_reagent(self, laboratory, reagent):
        laboratory.add_reagent(reagent)

    def refine_reagents(self, laboratory):
        laboratory.refine_reagents()


class Laboratory:
    def __init__(self):
        self.potions = []
        self.herbs = []
        self.catalysts = []

    def mix_potion(self, ingredient1, ingredient2):
        if isinstance(ingredient1, (Herb, Catalyst)) and isinstance(ingredient2, (Herb, Catalyst)):
            potion = Potion(name="Super Potion", stat_attribute="attack", boost_attribute=10)
            self.potions.append(potion)
            return potion
        else:
            print("Invalid ingredients for potion mixing.")
            return None

    def add_reagent(self, reagent):
        if isinstance(reagent, Herb):
            self.herbs.append(reagent)
        elif isinstance(reagent, Catalyst):
            self.catalysts.append(reagent)

    def refine_reagents(self):
        for herb in self.herbs:
            herb.refine()
        for catalyst in self.catalysts:
            catalyst.refine()

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
