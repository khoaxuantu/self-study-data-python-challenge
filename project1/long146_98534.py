def convert_units(value, from_unit, to_unit):
  

  # Conversion factors dictionar
  conversion_factors = {
      "length": {
          "cm": 1,
          "m": 100,
          "km": 100000,
          "in": 2.54,
          "ft": 30.48,
      },
      "temperature": {
          "C": lambda x: x,
          "F": lambda x: (x * 9/5) + 32,
          "K": lambda x: x + 273.15,
      },
      "volume": {
          "mL": 1,
          "L": 1000,
          "gal": 3785.41,
      },
  }

  
  if from_unit not in conversion_factors[get_unit_category(from_unit)] or to_unit not in conversion_factors[get_unit_category(to_unit)]:
    raise ValueError("Invalid units. Please choose units from the same category (length, temperature, volume).")


  conversion_factor = conversion_factors[get_unit_category(from_unit)][from_unit] / conversion_factors[get_unit_category(to_unit)][to_unit]


  return value * conversion_factor

def get_unit_category(unit):
 
  categories = {
      "cm": "length",
      "m": "length",
      "km": "length",
      "in": "length",
      "ft": "length",
      "C": "temperature",
      "F": "temperature",
      "K": "temperature",
      "mL": "volume",
      "L": "volume",
      "gal": "volume",
  }
  return categories.get(unit, None)  # Return None for invalid units




value1 = 10
from_unit = "cm"
to_unit = "m"



try:
  converted_value = convert_units(value1, from_unit, to_unit)
  print(f"{value1} {from_unit} is equal to {converted_value:.2f} {to_unit}")
except ValueError as e:
  print(e)

convert_units(200, 'C', 'F')

#Limiting the decimal points (2f) causes the output cannot show the answer correctly. Please be careful for the next project!