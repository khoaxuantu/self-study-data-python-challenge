#Exception func
class BadInputError (Exception): # syntax convention?
  """
  Dude, we have not reached the OOP or custom error topic -_-
  """
  def __init__ (self,message):
    self.message = message

#convertion func -- Typo ~
def convertion (input_unit, input_num):
  #convert the number into smallest unit
  if input_unit.lower () in ['nm', 'nanometer']: # Syntax convention?
    nm_num = input_num
  elif input_unit.lower () in ['um', 'micrometer']:
    nm_num = input_num * (10**3)
  elif input_unit.lower () in ['mm', 'millimeter']:
    nm_num = input_num * (10**6)
  elif input_unit.lower () in ['cm', 'centimeter']:
    nm_num = input_num * (10**7)
  elif input_unit.lower () in ['m', 'meter']:
    nm_num = input_num * (10**9)
  elif input_unit.lower () in ['m', 'kilometer']:
    nm_num = input_num * (10**12)

  #converted metric dict
  result_dict = {
      'nanometer': nm_num,
      'micrometer': nm_num / (10**3),
      'millimeter': nm_num / (10**6),
      'centimeter': nm_num / (10**7),
      'meter' : nm_num / (10**9),
      'kilometer': nm_num / (10**12)
  }
  return result_dict

print ("WELCOME TO CONVERTION.")
print ()
unit_list = ['nm', 'um', 'mm', 'cm', 'm', 'km',  'Nanometer', 'Micrometer', 'Millimeter', 'Centimeter', 'Meter', 'Kilometer']

while True:
  #ask user for input
  try:
    user_unit = input ('Enter starting unit ( Nanometer, Micrometer, Millimeter, Centimeter, Meter, Kilometer) ("Q" to quit): ')
    if user_unit.lower () == 'q':
      break
    if user_unit not in unit_list:
      raise BadInputError ("Please enter valid unit in list!")
    convert_unit = input ('Enter unit to convert to ( Nanometer, Micrometer, Millimeter, Centimeter, Meter, Kilometer): ')
    if convert_unit not in unit_list:
      raise BadInputError ("Please enter valid unit in list!")
    user_input = input (f'Enter a number in {user_unit}: ')
    try:
      user_number = int (user_input)
    except:
      raise BadInputError ("Please enter a number!")
  except BadInputError as e:
    print (e.message)
    print ()
  else:
    #Call out convertion dict
    result_dict = convertion (user_unit, user_number)
    print ('Convertion: ')
    #format the returned datatype
    result = result_dict[convert_unit.lower ()]
    if result_dict[convert_unit.lower ()] % 1 == 0:
      result = int (result)
    #display result
    print (f"{user_number} {user_unit} = {result} {convert_unit}")
    print ()
print ('Thank you!')

"""
The syntax is awkward to me, perhaps. It's different from the usual conventions.
"""

