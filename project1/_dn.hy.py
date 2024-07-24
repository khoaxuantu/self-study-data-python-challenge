#Please careful with the output. Limiting the decimal points (2f) causes the output cannot show some answers correctly.
def convert(value, from_value, to_value):
   conversion_list = {
      "mm": 0.001,  # millimet to met
      "cm": 0.01,   # centimet to met
      "m": 1.0,    # met to met
      "in": 0.0254, # inch to met
      "ft": 0.3048, # feet to met
      "um": 0.000001, # micromet to met
      "nm": 0.000000001, # nanomet to met
  }
   if from_value not in conversion_list or to_value not in conversion_list:
        raise ValueError("Nhập sai đơn vị chúng tôi có.")

   factor = conversion_list[from_value] / conversion_list[to_value]

   converted_value = value * factor

   return converted_value, to_value

value = float(input("Nhập giá trị muốn chuyển đổi "))

from_value = input("Bạn muốn đổi từ đơn vị: (mm, cm, m, in, ft, um, nm): ").lower()

to_value = input("Bạn muốn đổi sang đơn vị: (mm, cm, m, in, ft, um, nm): ").lower()

converted_value, new_unit = convert(value, from_value, to_value)

print(f"{value} {from_value} bằng {converted_value:.2f} {new_unit}")