nhap_gia_tri = float(input('Nhập giá trị: '))
nhap_don_vi1 = input('Nhập đơn vị (mm, cm, m, km, yd, ft, in): ').lower()
nhap_don_vi2 = input('Nhập đơn vị muốn chuyển đổi (mm, cm, m, km, yd, ft, in): ').lower()

def chuyen_doi(gia_tri, don_vi1, don_vi2):
    # Chuyển các đơn vị khác về mm trước
    if don_vi1 == 'mm':
        mm = gia_tri
    elif don_vi1 == 'cm':
        mm = gia_tri * 10
    elif don_vi1 == 'm':
        mm = gia_tri * 1000
    elif don_vi1 == 'km':
        mm = gia_tri * 1000000
    elif don_vi1 == 'yd':
        mm = gia_tri * 914.4
    elif don_vi1 == 'ft':
        mm = gia_tri * 304.8
    elif don_vi1 == 'in':
        mm = gia_tri * 25.4
    else:
        return 'Đơn vị không hợp lệ'

    # Chuyển từ mm sang đơn vị đích
    if don_vi2 == 'mm':
        ket_qua = mm
    elif don_vi2 == 'cm':
        ket_qua = mm / 10
    elif don_vi2 == 'm':
        ket_qua = mm / 1000
    elif don_vi2 == 'km':
        ket_qua = mm / 1000000
    elif don_vi2 == 'yd':
        ket_qua = mm / 914.4
    elif don_vi2 == 'ft':
        ket_qua = mm / 304.8
    elif don_vi2 == 'in':
        ket_qua = mm / 25.4
    else:
        return 'Đơn vị không hợp lệ'

    return f'{gia_tri} {don_vi1} = {ket_qua} {don_vi2}'

ket_qua = chuyen_doi(nhap_gia_tri, nhap_don_vi1, nhap_don_vi2)
print(ket_qua)

#Good job! You nailed it :3