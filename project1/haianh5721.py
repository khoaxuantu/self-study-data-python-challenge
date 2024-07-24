option={1:"cm",2:"mm",3:"m",4:"km",5:"microM",6:"nanoM"}
print("chon don vi ban muon chuyen doi")
print("1.cm")
print("2.mm")
print("3.m")
print("4.km")
print("5.microM")
print("6.nanoM")

i = float(input())
num =float(input("nhập số bạn muốn chuyển đổi\n"))
if i == 1:
    print("chọn tiếp đơn vị bạn muốn đổi thành")
    print("1.mm")
    print("2.m")
    print("3.km")
    print("4.microM")
    print("5.nanoM")
    i1 = int(input())
    if i1 == 1:
        print(num,"cm =" ,num*10,"mm")
    elif i1 == 2:
        print(num,"cm =" ,num/100,"m")
    elif i1 == 3:
        print(num,"cm =" ,f'{num/10000:.0f}',"km")
    elif i1 == 4:
        print(num,"cm =" ,f'{num/10000:.0f}',"microM")
    elif i1 == 5:
        print(num,"cm =" ,f'{num/10000000:0f}',"nanoM")
elif i == 2:
    print("chọn tiếp đơn vị bạn muốn đổi thành")
    print("1.cm")
    print("2.mm")
    print("3.km")
    print("4.microM")
    print("5.nanoM")
    i1 = int(input())
    if i1 == 1:
        print(num,"mm =" ,num/10,"cm")
    elif i1 == 2:
        print(num,"mm =" ,num/1000,"m")
    elif i1 == 3:
        print(num,"mm =" ,f'{num/10000000:.0f}',"km")
    elif i1 == 4:
        print(num,"mm =" ,f'{num*10000:.0f}',"microM")
    elif i1 == 5:
        print(num,"mm =" ,f'{num*10000000:0f}',"nanoM")
elif i == 3:
    print("chọn tiếp đơn vị bạn muốn đổi thành")
    print("1.cm")
    print("2.mm")
    print("3.km")
    print("4.microM")
    print("5.nanoM")
    i1 = int(input())
    if i1 == 1:
        print(num,"m =" ,num*100,"cm")
    elif i1 == 2:
        print(num,"m =" ,num/1000,"mm")
    elif i1 == 3:
        print(num,"m =" ,f'{num/1000:.0f}',"km")
    elif i1 == 4:
        print(num,"m =" ,f'{num*1000000:.0f}',"microM")
    elif i1 == 5:
        print(num,"m  =" ,f'{num*1000000000:0f}',"nanoM")
elif i == 4:
    print("chọn tiếp đơn vị bạn muốn đổi thành")
    print("1.cm")
    print("2.mm")
    print("3.m")
    print("4.microM")
    print("5.nanoM")
    i1 = int(input())
    if i1 == 1:
        print(num,"km =" ,num*100000,"cm")
    elif i1 == 2:
        print(num,"km =" ,num*1000000,"mm")
    elif i1 == 3:
        print(num,"km =" ,f'{num*1000:.0f}',"m")
    elif i1 == 4:
        print(num,"km =" ,f'{num*1000000000:.0f}',"microM")
    elif i1 == 5:
        print(num,"km  =" ,f'{num*1000000000000:0f}',"nanoM")
elif i == 5:
    print("chọn tiếp đơn vị bạn muốn đổi thành")
    print("1.cm")
    print("2.mm")
    print("3.m")
    print("4.km")
    print("5.nanoM")
    i1 = int(input())
    if i1 == 1:
        print(num,"microM =" ,num/10000,"cm")
    elif i1 == 2:
        print(num,"microM =" ,num/1000,"mm")
    elif i1 == 3:
        print(num,"microM =" ,f'{num/1000000:.0f}',"m")
    elif i1 == 4:
        print(num,"microM =" ,f'{num/1000000000:.0f}',"km")
    elif i1 == 5:
        print(num,"microM  =" ,f'{num*1000:0f}',"nanoM")
elif i == 6:
    print("chọn tiếp đơn vị bạn muốn đổi thành")
    print("1.cm")
    print("2.mm")
    print("3.m")
    print("4.km")
    print("5.microM")
    i1 = int(input())
    if i1 == 1:
        print(num,"nanoM =" ,num/10000000,"cm")
    elif i1 == 2:
        print(num,"nanoM =" ,num/1000000,"mm")
    elif i1 == 3:
        print(num,"nanoM =" ,f'{num/1000000000:.0f}',"m")
    elif i1 == 4:
        print(num,"nanoM =" ,f'{num/1000000000000:.0f}',"km")
    elif i1 == 5:
        print(num,"nanoM  =" ,f'{num/1000:0f}',"micro")


# Nice work here! But to shorten your code, you can put the output options in a string or as a function and call it in each cases.
'''
def choice():
    units = "chọn tiếp đơn vị bạn muốn đổi thành \n 1. cm \n 2. mm \n 3. m \n 4. km \n 5. microM \n 6. nanoM "
    print(units)
'''
# Keep up the good work!

