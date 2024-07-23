def convert_units(value, from_unit, to_unit):
    list = {'µm' : 1,
           'mm' : 1000,
           'cm' : 10000,
           'dm' : 100000,
           'm' : 1000000,
           'km' : 1000000000}
    value_in_µm = value * list[from_unit.lower()]
    result = value_in_µm / list[to_unit.lower()]
    return result
def main():
    from_unit = input('Enter the unit of measurement for movement (µm,mm,cm,dm,m,km): ') # Reviewer: Need out of bound input handler
    to_unit = input('Enter the unit of measure to convert to (µm,mm,cm,dm,m,km): ') # Reviewer: Need out of bound input handler
    value = float(input(f"Enter measurements starting with {from_unit}: "))
    result = convert_units(value, from_unit, to_unit)
    print(print(f"Result: {value} {from_unit} = {result} {to_unit}"))
if __name__ == "__main__":
    main()

