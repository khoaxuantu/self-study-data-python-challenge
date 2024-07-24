length_category = [
    (1, 'Meter', 1.0),
    (2, 'Kilometer', 0.001),
    (3, 'Centimeter', 100.0),
    (4, 'Milimeter', 1000.0),
    (5, 'Micrometer', 1e6),
    (6, 'Nanometer', 1e9)
 ]

for unit in length_category:
  print(f'{unit[0]} {unit[1]}')
unit_numbers = [unit[0] for unit in length_category]

while True:
  try:
    from_input = int(input('From: '))
    if from_input in unit_numbers:
      break
    else:
      print('Invalid value. Enter again.')
  except ValueError:
    print('Invalid value. Enter again.')

while True:
  try:
    to_input = int(input('To: '))
    if to_input in unit_numbers:
      break
    else:
      print('Invalid value. Enter again.')
  except ValueError:
    print('Invalid value. Enter again.')

while True:
  user_input = input('Enter a value: ')
  try:
    value = float(user_input)
    if value>=0:
      break
    else:
      print('Invalid value. Enter again.')
  except ValueError:
    print('Invalid value. Enter again.')

from_unit = length_category[from_input-1]
to_unit = length_category[to_input-1]
print(f'{value} {from_unit[1]} = {value/from_unit[2]*to_unit[2]} {to_unit[1]}')

#Keep up the good works!