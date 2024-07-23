class UnitConverter:
    """
    Reviwer: Dude we have not reached the OOP topic yet -_-
    """
    def __init__(self):
        self.conversion_factors = {
            "Meter": 1,
            "Kilometer": 0.001,
            "Centimeter": 100,
            "Millimeter": 1000,
            "Micrometer": 1e6,
            "Nanometer": 1e9,
            "Mile": 0.000621371,
            "Yard": 1.093613298,
            "Foot": 3.280839895,
            "Inch": 39.3701,
            "Light Year": 1.057e-16
        }
        self.units = list(self.conversion_factors.keys())

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        direct_conversion_factor = self.conversion_factors[to_unit] / self.conversion_factors[from_unit]
        return value * direct_conversion_factor

    def display_units(self) -> list:
        for i, unit in enumerate(self.units, 1):
            print(f"{i}. {unit}")
        return self.units

class UserInterface:
    def __init__(self):
        self.converter = UnitConverter()

    def get_unit_choice(self, prompt: str) -> str:
        while True:
            units = self.converter.display_units()
            choice = input(prompt)
            if choice.isdigit() and 1 <= int(choice) <= len(units):
                return units[int(choice) - 1]
            else:
                print(f"Please enter a number from 1 to {len(units)}.")

    def get_value_input(self) -> float:
        while True:
            try:
                value_input = input("\nEnter the value you want to convert: ")
                return float(value_input)
            except ValueError:
                print("Please enter a valid number!")

    def run(self):
        print("Enter units:")
        from_unit = self.get_unit_choice("Select the unit you want to convert from (enter the number): ")
        print("\nUnits you want to convert to:")
        to_unit = self.get_unit_choice("Select the unit you want to convert to (enter the number): ")
        value = self.get_value_input()
        result = self.converter.convert(value, from_unit, to_unit)
        print(f"\nResult: {value} {from_unit} = {format(result, '.10g')} {to_unit}")

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()

# Reviwer: The code looks clean. Spotted one smurf here :xien:

