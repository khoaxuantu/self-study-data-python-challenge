def Unit_Converter_Weight(from_unit, to_unit, unit_value):
      if from_unit == to_unit:
          return unit_value
      
      # Chuyển đổi tất cả về gram trước
      if from_unit == 'kg':
          grams = unit_value * 1000
      elif from_unit == 'g':
          grams = unit_value
      elif from_unit == 'mg':
          grams = unit_value / 1000
      elif from_unit == 'lb':
          grams = unit_value * 453.592
      elif from_unit == 'oz':
          grams = unit_value * 28.3495
      elif from_unit == 'ton':
          grams = unit_value * 1000000
      else:
          return None
      
      # Chuyển từ gram sang đơn vị đích
      if to_unit == 'kg':
          return grams / 1000
      elif to_unit == 'g':
          return grams
      elif to_unit == 'mg':
          return grams * 1000
      elif to_unit == 'lb':
          return grams / 453.592
      elif to_unit == 'oz':
          return grams / 28.3495
      elif to_unit == 'ton':
          return grams / 1000000
      else:
          return None

def main():
    units = ['kg', 'g', 'mg', 'lb', 'oz', 'ton']
    print("Chuyển đổi đơn vị trọng lượng")
    print("Các đơn vị hỗ trợ: kg, g, mg, lb, oz, ton")
    
    while True:
        from_unit = input("Nhập đơn vị gốc (hoặc 'q' để thoát): ").lower()
        if from_unit == 'q':
            break
        
        to_unit = input("Nhập đơn vị đích (hoặc 'q' để thoát): ").lower()
        if to_unit == 'q':
            break
        
        if from_unit not in units or to_unit not in units:
            print("Đơn vị không hợp lệ. Vui lòng chọn từ: kg, g, mg, lb, oz, ton")
            continue
        
        try:
            unit_value = float(input(f"Nhập giá trị cần chuyển đổi từ {from_unit}: "))
            converted_value = Unit_Converter_Weight(from_unit, to_unit, unit_value)
            if converted_value is not None:
                print(f"Kết quả: {unit_value} {from_unit} = {converted_value:.4f} {to_unit}")
            else:
                print("Không thể thực hiện chuyển đổi.")
        except ValueError:
            print("Giá trị không hợp lệ. Vui lòng nhập một số.")

if __name__ == "__main__":
    main()

# Keep up the good work!