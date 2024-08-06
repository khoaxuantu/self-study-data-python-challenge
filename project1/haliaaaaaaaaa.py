# Reviewer: Don't be if...else slave dude -_-
def converters(input_a, input_b, value):
    if input_a == 'Yard':
        if input_b == 'Meter':
            return value * 0.9144
        elif input_b == 'Foot':
            return value * 3
        elif input_b == 'Inch':
            return value * 36
        elif input_b == 'Mile':
            return value / 1760
        elif input_b == 'KiloMeter':
            return value * 0.0009144
    if input_a == 'Meter':
        if input_b == 'Yard':
            return value / 3
        elif input_b == 'Foot':
            return value * 3.281
        elif input_b == 'Inch':
            return value * 39.37
        elif input_b == 'Mile':
            return value / 1609.344
        elif input_b == 'KiloMeter':
            return value / 1000
    if input_a == 'Foot':
        if input_b == 'Yard':
            return value / 3
        elif input_b == 'Meter':
            return value / 3.281
        elif input_b == 'Inch':
            return value * 12
        elif input_b == 'Mile':
            return value / 5280
        elif input_b == 'KiloMeter':
            return value / 3281
    if input_a == 'Inch':
        if input_b == 'Yard':
            return value / 36
        elif input_b == 'Meter':
            return value / 39.37
        elif input_b == 'Foot':
            return value / 12
        elif input_b == 'Mile':
            return value / 63360
        elif input_b == 'KiloMeter':
            return value / 39370
    if input_a == 'Mile':
        if input_b == 'Yard':
            return value * 1760
        elif input_b == 'Meter':
            return value * 1609.344
        elif input_b == 'Foot':
            return value * 5280
        elif input_b == 'Inch':
            return value * 63360
        elif input_b == 'KiloMeter':
            return value * 1.60934


def main():
    # get input_a from user

    # Reviewer: Please handle the out of bound cases
    input_a = input("Enter Starting Unit of Measurement(Yard, Inch, Meter, Foot, Mile, KiloMeter): ")
    input_b = input("Enter Unit of Measurement to Convert to (Yard, Inch, Meter, Foot, Mile, KiloMeter): ")
    value = float(input("Enter value: "))
    result = converters(input_a, input_b, value)
    print(f"{value} {input_a} = {result} {input_b}")

if __name__ == "__main__":
    main()

