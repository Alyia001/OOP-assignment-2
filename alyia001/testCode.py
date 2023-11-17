#File: testCode.py
#Description: Main Code for the implementation of a common RPG uml design
#Author: Ian Amir Al Faily
#StudentID:110416702
#EmailID: Alyia001
#This is my own work as defined by the University's Academic Misconduct Policy.

import unittest
from mainCode import Potion, Reagent, Laboratory, Alchemist

class TestAlchemist(unittest.TestCase):
    def test_potion_calculation_super_potion(self):
        herb = Reagent("Irit", 1.0)
        catalyst = Reagent("Eye of Newt", 4.3)
        super_attack_potion = Potion("Super Attack", "attack", 0)

        super_attack_potion.calculate_boost(herb)
        self.assertEqual(super_attack_potion.boost_attribute, 5.45)  # Adjust based on your calculation logic

    def test_potion_calculation_extreme_potion(self):
        herb = Reagent("Irit", 1.0)
        catalyst = Reagent("Eye of Newt", 4.3)
        super_attack_potion = Potion("Super Attack", "attack", 0)
        extreme_attack_potion = Potion("Extreme Attack", "attack", 0)

        super_attack_potion.calculate_boost(herb)
        extreme_attack_potion.calculate_boost(super_attack_potion)
        self.assertEqual(extreme_attack_potion.boost_attribute, 16.35)  # Adjust based on your calculation logic

    def test_potion_mixing(self):
        laboratory = Laboratory()
        herb = Reagent("Irit", 1.0)
        catalyst = Reagent("Eye of Newt", 4.3)
        super_attack_potion = Potion("Super Attack", "attack", 0)

        laboratory.add_reagent(herb)
        laboratory.add_reagent(catalyst)
        laboratory.mix_potion(herb, super_attack_potion)
        self.assertIn(super_attack_potion, laboratory.potions)

if __name__ == '__main__':
    unittest.main()
