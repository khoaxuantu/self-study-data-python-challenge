# Reviewer: Great to see some actual comments here
def convert_length(from_unit, to_unit, value):
  """Converts a length value between different units.

  Args:
      from_unit: The unit the value is currently in (nm,um,mm,cm,m,km).
      to_unit: The unit you want to convert the value to (nm,um,mm,cm,m,km).
      value: The length value to be converted.

  Returns:
      The converted length value in the desired unit.
  """

  # Conversion factors dictionary
  conversion_factors = {
      "nm": {  # Conversion factors from nanometer
          "nm": 1,
          "um": 1e-3,  # 1e-3 is scientific notation for 0.001
          "mm": 1e-6,
          "cm": 1e-7,
          "m": 1e-9,
          "km": 1e-12,
      },
      "um": {  # Conversion factors from micrometer
          "nm": 1e+3,
          "um": 1,
          "mm": 1e-3,
          "cm": 1e-4,
          "m": 1e-6,
          "km": 1e-9,
      },
      "mm": {  # Conversion factors from millimeter
          "nm": 1e+6,
          "um": 1e+3,
          "mm": 1,
          "cm": 1e-1,
          "m": 1e-3,
          "km": 1e-6,
      },
      "cm": {  # Conversion factors from centimeter
          "nm": 1e+7,
          "um": 1e+4,
          "mm": 1e+1,
          "cm": 1,
          "m": 1e-2,
          "km": 1e-5,
      },
      "m": {  # Conversion factors from meter
          "nm": 1e+9,
          "um": 1e+6,
          "mm": 1e+3,
          "cm": 1e+2,
          "m": 1,
          "km": 1e-3,
      },
      "km": {  # Conversion factors from kilometer
          "nm": 1e+12,
          "um": 1e+9,
          "mm": 1e+6,
          "cm": 1e+5,
          "m": 1e+3,
          "km": 1,
      },
  }

  # Check for valid units
  if from_unit not in conversion_factors or to_unit not in conversion_factors:
    raise ValueError("Invalid unit(s). Supported units: nm, um, mm, cm, m, km")

  # Perform the conversion
  conversion_factor = conversion_factors[from_unit][to_unit]
  converted_value = value * conversion_factor

  return converted_value

# Example usage
while True:
  try:
    from_unit = input("Enter Starting Unit of Measurement (nm, um, mm, cm, m, km): ").lower()
    to_unit = input("Enter Unit of Measurement to Convert to (nm, um, mm, cm, m, km): ").lower()
    value = float(input("Enter the value to convert: "))

    converted_value = convert_length(from_unit, to_unit, value)
    print(f"{value} {from_unit} is equal to {converted_value:.2f} {to_unit}.")
    break  # Exit the loop after successful conversion
  except ValueError as e:
    print(e)  # Print error message for invalid units

# Noice

