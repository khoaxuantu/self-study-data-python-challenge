f_unit={"m", "cm", "inch", "foot","yard", "km"}
t_unit={"m", "cm", "inch", "foot","yard", "km"}

# Nhập đơn vị bắt đầu từ người dùng
from_unit = input("Enter Starting Unit of Measurement (m, cm, inch, foot, yard, km): ").lower()
# Check from_unit
while from_unit not in f_unit:
    from_unit = input("Invalid input. Re-enter the unit you want to convert (m, cm, inch, foot, yard, km): ").lower()
    # Nhập đơn vị muốn chuyển đổi từ người dùng
to_unit = input("Enter Unit of Measurement to convert to: ").lower() #You can write out the units available here <3
    # Check to_unit
while to_unit not in t_unit:
    to_unit = input(f"Invalid input. Re-enter the unit you want to convert from {from_unit} to: ").lower()

#Nhập giá trị từ người dùng và check value
while True:
    val = input(f"Enter Starting Measurement in {from_unit}: ")
    try:
        val= float(val)
        break
    except ValueError:
        print("Invalid input. Please enter a valid floating point number.")
        
def convert_length(val, from_unit, to_unit):
# Định nghĩa hệ số chuyển đổi đến m
    SI = {
            'cm': 0.01,    
            'm': 1.0,        
            'km': 1000,    
            'foot': 0.3048,    
            'yard': 0.9144, 
            'inch': 0.0254}
    # Chuyển giá trị từ đơn vị đầu vào về m
    value_in_meters = val * SI[from_unit]
    # Chuyển giá trị từ m về đơn vị đích
    return(value_in_meters/SI[to_unit])
result= convert_length(val, from_unit, to_unit)
print(f"Result: {val} {from_unit} = {result} {to_unit}")

#Overall, good job !