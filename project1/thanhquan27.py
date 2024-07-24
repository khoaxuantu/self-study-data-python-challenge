def convert_units(value, from_unit, to_unit, category): #hàm chuyển đổi
    # Định nghĩa các hệ số chuyển đổi cho từng loại đơn vị (VD: 1 giờ = 60 phút = 3600 giây; 1$ = 0.85 euro = 23000,....)
    conversion_factors = {
        "chiều dài": {
            "inches": {"inches": 1, "feet": 1/12, "yards": 1/36},
            "feet": {"inches": 12, "feet": 1, "yards": 1/3},
            "yards": {"inches": 36, "feet": 3, "yards": 1}
        },
        "khối lượng": {
            "grams": {"grams": 1, "kilograms": 1/1000, "pounds": 1/453.592},
            "kilograms": {"grams": 1000, "kilograms": 1, "pounds": 2.20462},
            "pounds": {"grams": 453.592, "kilograms": 0.453592, "pounds": 1}
        },
        "thời gian": {
            "seconds": {"seconds": 1, "minutes": 1/60, "hours": 1/3600},
            "minutes": {"seconds": 60, "minutes": 1, "hours": 1/60},
            "hours": {"seconds": 3600, "minutes": 60, "hours": 1}
        },
        "tiền tệ": {
            "usd": {"usd": 1, "eur": 0.85, "vnd": 23000},
            "eur": {"usd": 1.18, "eur": 1, "vnd": 27000},
            "vnd": {"usd": 1/23000, "eur": 1/27000, "vnd": 1}
        },
        "áp suất": {
            "pascals": {"pascals": 1, "atmospheres": 1/101325, "psi": 1/6894.76},
            "atmospheres": {"pascals": 101325, "atmospheres": 1, "psi": 14.6959},
            "psi": {"pascals": 6894.76, "atmospheres": 1/14.6959, "psi": 1}
        }
    }
    
    # Kiểm tra tính hợp lệ của các tham số đầu vào, nghĩa là nếu các tham số nhập vào không có trong dict được lập ban đầu sẽ được tính là không hợp lệ (1 trong 3 thằng là True) -> trả về None
    if category not in conversion_factors or from_unit not in conversion_factors[category] or to_unit not in conversion_factors[category][from_unit]:
        return None
    
    # Tính toán giá trị chuyển đổi
    factor = conversion_factors[category][from_unit][to_unit] #Lấy hệ số chuyển đổi từ from_unit sang to_unit dựa trên loại đơn vị category.
    converted_value = value * factor #Tính giá trị chuyển đổi bằng cách nhân value với hệ số chuyển đổi

    return converted_value #Trả về giá trị đã chuyển đổi

if __name__ == "__main__":
    # Nhập vào loại đơn vị, đơn vị và giá trị ban đầu
    category = input("Nhập vào đơn vị đo lường (chiều dài, khối lượng, thời gian, tiền tệ, áp suất): ").lower()
    from_unit = input("Muốn đổi từ: ").lower()
    to_unit = input("Đổi sang: ").lower()
    value = float(input(f"Nhập vào giá trị cần đổi ở {from_unit.capitalize()}: "))

    # Thực hiện chuyển đổi
    result = convert_units(value, from_unit, to_unit, category)

    # In kết quả
    if result is not None: #Nếu inputs đều hợp lệ -> in kết quả
        print(f"Result: {value} {from_unit.capitalize()} = {result} {to_unit.capitalize()}")
    else:
        print("Invalid units or category.") # inputs không hợp lệ -> trả về Invalid

#Good job!