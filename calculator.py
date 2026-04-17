# calculator.py
# Team: Alex Tang and Nick Heo
# Project: Python Fitness & Macro Calculator

class User:
    def __init__(self, age, gender, weight_kg, height_cm, activity_level, goal):
        self.age = age
        self.gender = gender.lower()
        self.weight_kg = weight_kg
        self.height_cm = height_cm
        self.activity_level = activity_level
        self.goal = goal
        self.bmr = 0
        self.tdee = 0
        self.macros = {}

    # Alex: Handle main calorie calculations
    def calculate_bmr_tdee(self):
        """
        Calculates Basal Metabolic Rate using the Mifflin-St Jeor equation
        and multiplies by activity multiplier to get TDEE.
        """
        # Mifflin-St Jeor Equation
        if self.gender == 'male':
            self.bmr = (10 * self.weight_kg) + (6.25 * self.height_cm) - (5 * self.age) + 5
        elif self.gender == 'female':
            self.bmr = (10 * self.weight_kg) + (6.25 * self.height_cm) - (5 * self.age) - 161
        else:
            # Defaulting to a generic average if not specified
            self.bmr = (10 * self.weight_kg) + (6.25 * self.height_cm) - (5 * self.age)

        # TODO: Add activity level multipliers to calculate TDEE
        self.tdee = self.bmr * 1.2 # Placeholder multiplier for sedentary
        return self.tdee

    # Nick: Split calories into macros
    def calculate_macros(self):
        """
        Splits TDEE into protein, carbs, and fats based on the user's goal.
        """
        # TODO: Implement macro splits based on self.goal (e.g., 'cut', 'bulk', 'maintain')
        pass

    # Alex: Display results
    def format_output_report(self):
        """
        Displays everything in a clean, readable summary in the terminal.
        """
        # TODO: Format the print statements cleanly
        pass

# Nick: Handle input
def get_user_input():
    """
    Handles command line input and validates values.
    """
    print("Welcome to the Fitness & Macro Calculator!")
    # TODO: Add input prompts (age, weight, height, etc.) and validation
    pass

if __name__ == "__main__":
    # Temporary test data to make sure our class instantiates correctly
    test_user = User(age=25, gender="male", weight_kg=80, height_cm=180, activity_level="moderate", goal="maintain")
    test_user.calculate_bmr_tdee()
    print(f"Test Setup Complete. BMR is roughly: {test_user.bmr}")