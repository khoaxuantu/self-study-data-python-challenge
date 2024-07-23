from decimal import Decimal, getcontext
getcontext().prec = 2

conversion_factors = {
    'inches': {'inches': Decimal(1), 'feet': Decimal(1)/Decimal(12), 'yards': Decimal(1)/Decimal(36), 'cm': Decimal(2.54), 'm': Decimal(0.0254), 'km': Decimal(0.0000254), 'mm': Decimal(25.4)},
    'feet': {'inches': Decimal(12), 'feet': Decimal(1), 'yards': Decimal(1)/Decimal(3), 'cm': Decimal(30.48), 'm': Decimal(0.3048), 'km': Decimal(0.0003048), 'mm': Decimal(304.8)},
    'yards': {'inches': Decimal(36), 'feet': Decimal(3), 'yards': Decimal(1), 'cm': Decimal(91.44), 'm': Decimal(0.9144), 'km': Decimal(0.0009144), 'mm': Decimal(914.4)},
    'cm': {'inches': Decimal(1)/Decimal(2.54), 'feet': Decimal(1)/Decimal(30.48), 'yards': Decimal(1)/Decimal(91.44), 'cm': Decimal(1), 'm': Decimal(0.01), 'km': Decimal(0.00001), 'mm': Decimal(10)},
    'm': {'inches': Decimal(1)/Decimal(0.0254), 'feet': Decimal(1)/Decimal(0.3048), 'yards': Decimal(1)/Decimal(0.9144), 'cm': Decimal(100), 'm': Decimal(1), 'km': Decimal(0.001), 'mm': Decimal(1000)},
    'km': {'inches': Decimal(1)/Decimal(0.0000254), 'feet': Decimal(1)/Decimal(0.0003048), 'yards': Decimal(1)/Decimal(0.0009144), 'cm': Decimal(100000), 'm': Decimal(1000), 'km': Decimal(1), 'mm': Decimal(1000000)}
}

def convert_units(value, from_unit, to_unit):
    return Decimal(value) * conversion_factors[from_unit][to_unit]

def main():
    print("Unit Conversion Project - Python Challenge")
    
    value = input("Enter the value to convert: ")
    from_unit = input("Enter the unit to convert from (inches, feet, yards, cm, m, km): ").lower()
    to_unit = input("Enter the unit to convert to (inches, feet, yards, cm, m, km): ").lower()
    
    if from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
        result = convert_units(value, from_unit, to_unit)
        print(f"{value} {from_unit} = {result} {to_unit}")
    else:
        print("Invalid conversion units")

if __name__ == "__main__":
    main()

# Reviewer: Noice

