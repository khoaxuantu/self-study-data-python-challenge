#Length - Convert between "meters/kilometers/centimeters/yards/feet/inches"
#Convert between meters and kilometers:
def kilometers_to_meters(kilometers):
    return kilometers * 1000
def meters_to_kilometers(meters):
    return meters / 1000
#Convert between meters and centimeters:
def meters_to_centimeters(meters):
    return meters * 100
def centimeters_to_meters(centimeters):
    return centimeters / 100
#Convert between meters and yards:
def meters_to_yards(meters):
    return meters * 1.09361
def yards_to_meters(yards):
    return yards / 1.09361
#Convert between meters and feet:
def meters_to_feet(meters):
    return meters * 3.28084
def feet_to_meters(feet):
    return feet / 3.28084
#Convert between meters and inches
def meters_to_inches(meters):
    return meters * 39.3701
def inches_to_meters(inches):
    return inches / 39.3701
#Convert between kilometers and centimeters:
def kilometers_to_centimeters(kilometers):
    return kilometers * 100000
def centimeters_to_kilometers(centimeters):
    return centimeters / 100000
#Convert between kilometers and yards:
def kilometers_to_yards(kilometers):
    return kilometers * 1093.6133
def yards_to_kilometers(yards):
    return yards / 1093.6133
#Convert between kilometers and feet:
def kilometers_to_feet(kilometers):
    return kilometers * 3280.8399
def feet_to_kilometers(feet):
    return feet / 3280.8399
#Convert between kilometers and inches:
def kilometers_to_inches(kilometers):
    return kilometers * 39370.07874
def feet_to_kilometers(inches):
    return inches / 39370.07874
#Convert between centimeters and yards:
def yards_to_centimeters(yards):
    return yards * 0.01094
def centimeters_to_yards(centimeters):
    return centimeters / 0.01094
#Convert between centimeters and feet
def feet_to_centimeters(feet):
    return feet * 30.48
def centimeters_to_feet(centimeters):
    return centimeters / 30.48
#Convert between centimeters and inches:
def inches_to_centimeters(inches):
    return inches * 2.54
def centimeters_to_inches(centimeters):
    return centimeters / 2.54
#Convert between yards and feet:
def yards_to_feet(yards):
    return yards * 3
def feet_to_yards(feet):
    return feet / 3
#Convert between yards and inches:
def yards_to_inches(yards):
    return yards * 36
def inches_to_yards(inches):
    return inches / 36
#Convert between feet and inches:
def feet_to_inches(feet):
    return feet * 12
def inches_to_feet(inches):
    return inches / 12

#Example usage:
yards = 300
meters = yards_to_meters(yards)
print(f'{yards} yards = {meters:.2f} meters')

# Reviewer: I wish we have some abstract functions to handle all these methods

