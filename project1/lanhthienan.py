print("Các đơn vị hỗ trợ: meter, kilometer, centimeter, milimeter, mile, feet")

gia_tri = float(input("Nhập giá trị: "))
tu_don_vi = input("Đơn vị chuyển đổi từ (meter, kilometer, centimeter, milimeter, miles, feet): ")

if tu_don_vi not in ['meter', 'kilometer', 'centimeter', 'milimeter' 'mile', 'feet']:
    print("Đơn vị đầu vào không hợp lệ. Vui lòng thử lại.")
else:
    if tu_don_vi == 'meter':
        gia_tri_met = gia_tri
    elif tu_don_vi == 'kilometer':
        gia_tri_met = gia_tri * 1000
    elif tu_don_vi == 'centimeter':
        gia_tri_met == gia_tri *0.01 #"gia_tri_met" is not difined here so you can't compare it, I think you mean '=' here
    elif tu_don_vi == 'milimeter':
        gia_tri_met == gia_tri * 0.001 #The same comment goes here
    elif tu_don_vi == 'mile':
        gia_tri_met = gia_tri * 1609.34
    elif tu_don_vi == 'feet':
        gia_tri_met = gia_tri * 0.3048
    
    print("Các đơn vị mục tiêu có thể: meters, kilometers, centimeter, milimeter, miles, feet")
    den_don_vi = input("Đơn vị chuyển đổi đến (meter, kilometer, centimeter, milimeter, mile, feet): ")

    if den_don_vi not in ['meter', 'kilometer','centimeter', 'milimeter', 'mile', 'feet']:
        print("Đơn vị mục tiêu không hợp lệ. Vui lòng thử lại.")
    else:
        if den_don_vi == 'meter':
            ket_qua = gia_tri_met
        elif den_don_vi == 'kilometer':
            ket_qua = gia_tri_met / 1000
        elif den_don_vi == 'centimeter':
            ket_qua = gia_tri_met / 0.01
        elif den_don_vi == 'millimeter':
            ket_qua = gia_tri_met / 0.001
        elif den_don_vi == 'mile':
            ket_qua = gia_tri_met / 1609.34
        elif den_don_vi == 'feet':
            ket_qua = gia_tri_met / 0.3048
        
        print(f"{gia_tri} {tu_don_vi} = {ket_qua} {den_don_vi}")

#Good job overall! However, because of your mistyping, you only got 4/6 units right => 2 bonus points