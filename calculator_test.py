# test_calculator.py
# Team Members: Alex Tang and Nick Heo

import unittest
from calculator import UserProfile

class TestUserProfile(unittest.TestCase):

    def setUp(self):
        # 25-year-old dude who weighs 80kg and just wants to maintain
        self.user = UserProfile(25, "male", 80, 180, "moderate", "maintain")

    def test_calculate_bmr_tdee_male(self):
        # We did the math by hand first, so now we are just checking if the computer gets the exact same answers
        self.user.calculate_bmr_tdee()
        self.assertEqual(self.user.bmr, 1805)
        self.assertEqual(self.user.tdee, 2797.75)

    def test_calculate_bmr_tdee_female(self):
        # Girls have a slightly different math rule for calories, so we have to make sure the program switches to that different rule properly
        female_user = UserProfile(25, "female", 80, 180, "sedentary", "maintain")
        female_user.calculate_bmr_tdee()
        
        # Checking her specific math answers
        self.assertEqual(female_user.bmr, 1639)
        self.assertEqual(female_user.tdee, 1966.8)

    def test_calculate_macros_maintain(self):
        # Testing the macros when he wants to maintain
        self.user.calculate_bmr_tdee()
        macros = self.user.calculate_macros()
        
        # We give him his daily protein and fat first
        # Then, we check if the computer correctly gave all the leftover calories to his carbs
        self.assertEqual(macros["protein"], 160)
        self.assertEqual(macros["fats"], 64)
        self.assertEqual(macros["carbs"], 395)

    def test_calculate_macros_cut(self):
        # Testing the cut
        cut_user = UserProfile(25, "male", 80, 180, "moderate", "cut")
        cut_user.calculate_bmr_tdee()
        macros = cut_user.calculate_macros()
        
        # We take away 500 calories from his daily food limit.
        # Then we check if his carbs dropped down correctly, since he gets to eat less food 
        self.assertEqual(macros["carbs"], 270)

if __name__ == '__main__':
    unittest.main()