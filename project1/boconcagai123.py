def meter_to_centimeter(meter):
    return meter * 100
    
meter = float(1)
centimeter = meter_to_centimeter(meter)
print(f"{meter} meter = {centimeter:.0f} centimeter")

def inch_to_meter(inches):
    return inches * 0.0254

inches = float(4)
meter = inch_to_meter(inches)
print(f"{inches} inch = {meter:.4f} meter")

def mile_to_kilometer(mile):
    return mile * 1.60935

mile = float(100)
kilometer = mile_to_kilometer(mile)
print(f"{mile} mile = {kilometer:.3f} kilometer")

def centimeter_to_meter(centimeter):
    return centimeter / 100

centimeter = float(0.980)
meter = centimeter_to_meter(centimeter)
print(f"{centimeter} centimeter = {meter:4f} meter")

def yard_to_micrometer(yard):
    return yard * 914400

yard = float(2)
micrometer = yard_to_micrometer(yard)
print(f"{yard} yard = {micrometer:0f} micrometer")

def foot_to_centimeter(foot):
    return foot * 30.48

foot = float(3)
centimeter = foot_to_centimeter(foot)
print(f"{centimeter} centimeter = {foot:2f} centimeter") # If I'm not wrong, it should be foot on the right instead of centimeter

# Anyway, I will give you 4 points for the qualified conversions' logic

