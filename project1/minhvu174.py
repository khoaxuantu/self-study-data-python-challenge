##Creat dictionary and list for reference
convert_facts = {
    'Minute': {'Hour': 0.0166666667, 'Day': 0.0006944444, 'Week': 0.0000992063, 'Month': 0.0000228154, 'Year': 0.0000019013},
    'Hour': {'Minute': 60, 'Day': 0.0416666667, 'Week': 0.005952381, 'Month': 0.0013689254, 'Year': 0.0001140771},
    'Day': {'Minute': 1440, 'Hour': 24, 'Week': 0.1428571429, 'Month': 0.0328542094, 'Year': 0.0027378508},
    'Week': {'Minute': 10080, 'Hour': 168, 'Day': 7, 'Month': 0.2299794661, 'Year': 0.0191649555},
    'Month': {'Minute': 43830, 'Hour': 730.5, 'Day': 30.4375, 'Week': 4.3482142857, 'Year': 0.0833333333},
    'Year': {'Minute': 525960, 'Hour': 8766, 'Day': 365.25, 'Week': 52.178571429, 'Month': 12},
}

units = list(convert_facts.keys())

##Statement
while True:
    print("Available units: ", units)
    from_unit = input("Which unit do you want to convert?: ").capitalize()
    to_unit = input("Which unit do you want to convert it to?: ").capitalize()
    value = float(input("Enter the value: "))

    if from_unit in units and to_unit in units:
        result = round(value * convert_facts[from_unit][to_unit],2) 
        print(f"{value} {from_unit} = {result} {to_unit}")
    else:
        print("Invalid unit. Please try again with available units.")

    response = input("Do you want to convert again? (y/n): ")
    if response.lower()!= 'y':
        break

#Rounding the answers to 2f causes some outputs cannot be displayed properly
#Overall, nice work!