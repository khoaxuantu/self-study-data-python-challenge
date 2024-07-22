units = {
    'm': 1,
    'km': 0.001,
    'miles': 0.0006213689,
    'ft': 3.280839895,
    'cm': 100,
    'inch': 39.37007874,
    'mm': 1000,
}

while True:
    unit_in = input("Nhập đơn vị ban đầu (m, km, miles, ft, cm, inch, mm): ").lower()
    if unit_in in units:
        try:
          unit_out_list = []
          print("Nhập các đơn vị muốn chuyển sang (m, km, miles, ft, cm, inch, mm) để trống và nhấn Enter để kết thúc:")
          while True:
              unit_out = input("Nhập đơn vị: ").lower()
              if unit_out == "":
                  break
              if unit_out not in units:
                  print("Đơn vị chuyển sang không hợp lệ. Vui lòng thử lại.")
              elif unit_out in unit_out_list:
                  print("Đơn vị đã được nhập. Vui lòng thử lại.")
              else:
                  unit_out_list.append(unit_out)
        except ValueError:
            print("Giá trị nhập vào không hợp lệ. Vui lòng thử lại.")
            continue

        value = float(input("Nhập giá trị cần chuyển đổi: "))
        value_to_meters = value / units[unit_in]
        print(f"{value} {unit_in} is:")

        for unit in unit_out_list:
            converted_value = value_to_meters * units[unit]
            print(f"  {converted_value} {unit}")

        continue_convert = input("Bạn có muốn tiếp tục đổi không? (nhấn (n hoặc N) để tạm dừng nhấn phím bất kì để tiếp tục): ").lower()
        if continue_convert == 'n':
            break
    else:
        print("Đơn vị nhập vào không hợp lệ. Vui lòng thử lại.")

# Noice

