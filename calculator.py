# calculator.py
# Team Members: Alex Tang and Nick Heo
# Description: Program to calculate Basal Metabolic Rate, Total Daily Energy Expenditure, and daily macro splits
# Source: Mifflin, M. D., St Jeor, S. T., et al. (1990).

class UserProfile:
    def __init__(self, age, gender, weight_kg, height_cm, activity_level, goal):
        self.age = age
        self.gender = gender.lower()
        self.weight_kg = weight_kg
        self.height_cm = height_cm
        self.activity_level = activity_level.lower()
        self.goal = goal.lower()
        self.bmr = 0
        self.tdee = 0
        self.macros = {"protein": 0, "fats": 0, "carbs": 0}

    def calculate_bmr_tdee(self):
        """
        Calculates Basal Metabolic Rate (Mifflin-St Jeor) and Total Daily Energy Expenditure
        Primary Driver: Alex, Navigator: Nick
        """
        # Calculate BMR based on gender
        if self.gender == 'male':
            self.bmr = (10 * self.weight_kg) + (6.25 * self.height_cm) - (5 * self.age) + 5
        elif self.gender == 'female':
            self.bmr = (10 * self.weight_kg) + (6.25 * self.height_cm) - (5 * self.age) - 161
        else:
            # Default average if not male/female
            self.bmr = (10 * self.weight_kg) + (6.25 * self.height_cm) - (5 * self.age)

        # Standard TDEE Activity Multipliers
        multipliers = {
            "sedentary": 1.2,
            "light": 1.375,
            "moderate": 1.55,
            "active": 1.725,
            "very active": 1.9
        }
        
        multiplier = multipliers.get(self.activity_level, 1.2)
        self.tdee = self.bmr * multiplier
        return self.tdee

    def calculate_macros(self):
        """
        Splits TDEE into protein, carbs, and fats based on the user's fitness goal
        Primary Driver: Nick, Navigator: Alex
        """
        # Adjust target calories based on goal
        if self.goal == "cut":
            target_calories = self.tdee - 500
        elif self.goal == "bulk":
            target_calories = self.tdee + 500
        else:
            target_calories = self.tdee  # maintain

        # Standard macro split formula: Protein (2g per kg), Fats (0.8g per kg)
        # Protein = 4 calories/g, Fat = 9 calories/g, Carbs = 4 calories/g
        self.macros["protein"] = round(self.weight_kg * 2.0)
        self.macros["fats"] = round(self.weight_kg * 0.8)

        protein_cals = self.macros["protein"] * 4
        fat_cals = self.macros["fats"] * 9
        remaining_cals = target_calories - (protein_cals + fat_cals)

        # Assign remaining calories to carbs, ensuring it doesn't drop below 0
        self.macros["carbs"] = max(0, round(remaining_cals / 4))
        return self.macros

    def format_output_report(self):
        """
        Prints a clean summary of the calculated data to the terminal.
        Primary Driver: Alex, Navigator: Nick
        """
        print("\n" + "="*40)
        print("        FITNESS & MACRO REPORT        ")
        print("="*40)
        print(f"BMR (Basal Metabolic Rate): {self.bmr:.0f} calories")
        print(f"TDEE (Maintenance Calories): {self.tdee:.0f} calories")
        print("-" * 40)
        
        target = self.tdee
        if self.goal == "cut": 
            target -= 500
        elif self.goal == "bulk": 
            target += 500
        
        print(f"Daily Calorie Target for '{self.goal}': {target:.0f} calories")
        print(f"Protein: {self.macros['protein']}g")
        print(f"Fats: {self.macros['fats']}g")
        print(f"Carbs: {self.macros['carbs']}g")
        print("="*40 + "\n")


def get_user_input():
    """
    Handles command line input and basic data validation.
    Returns a populated UserProfile object.
    Primary Driver: Nick, Navigator: Alex
    """
    print("\n--- Welcome to the Python Fitness & Macro Calculator ---")
    try:
        age = int(input("Enter your age: "))
        gender = input("Enter your gender (male/female): ")
        weight_kg = float(input("Enter your weight in kg: "))
        height_cm = float(input("Enter your height in cm: "))
        
        print("\nActivity Levels: sedentary, light, moderate, active, very active")
        activity_level = input("Enter your activity level: ")
        
        print("\nGoals: cut, bulk, maintain")
        goal = input("Enter your primary goal: ")
        
        # Instantiate and return the class object
        return UserProfile(age, gender, weight_kg, height_cm, activity_level, goal)
        
    except ValueError:
        print("\n[Error] Invalid input detected. Please ensure you enter numbers for age, weight, and height.")
        return None

# Global scope invocation requirement
if __name__ == "__main__":
    current_user = get_user_input()
    
    if current_user is not None:
        current_user.calculate_bmr_tdee()
        current_user.calculate_macros()
        current_user.format_output_report()