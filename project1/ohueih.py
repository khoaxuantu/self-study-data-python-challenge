print("------")
print("Please Input Your Units of Measurement & Conversion!")
print("kilometer/ meter/ centimeter/ mile/ yard/ inch")
print("------")

M1 = input("Enter Your Unit of Measurement: ")
C1 = input("Enter Your Unit of Conversion: ")
V1 = float(input("Enter Your Value: "))
result = 0

# Don't be if...else slave bruh -.-
if M1 == C1:
        result = V1
        print('=> Result:', V1, M1,'=', result, C1)
else:

        if M1 == 'kilometer':
                if C1 == 'meter':
                        result = V1 * 1000
                        print('=> Result:', V1, M1,'=', result, C1)
                elif C1 == 'centimeter':
                        result = V1 * 1000000
                        print('=> Result:', V1, M1,'=', result, C1)
                elif C1 == 'mile':
                        result = V1 * 0.6213688756
                        print('=> Result:', V1, M1,'=', result, C1)
                elif C1 == 'yard':
                        result = V1 * 1093.6132983
                        print('=> Result:', V1, M1,'=', result, C1)
                elif C1 == 'inch':
                        result = V1 * 39370.07874
                        print('=> Result:', V1, M1,'=', result, C1)
                else:
                        print('** Error! Please Input Precise Conversion')

        elif M1 == 'meter':
                if C1 == 'kilometer':
                        result = V1 * 0.001
                        print('=> Result:', V1, M1,'=', result, C1)
                elif C1 == 'centimeter':
                        result = V1 * 100
                        print('=> Result:', V1, M1,'=', result, C1)
                elif C1 == 'mile':
                        result = V1 * 0.0006213689
                        print('=> Result:', V1, M1,'=', result, C1)
                elif C1 == 'yard':
                        result = V1 * 1.0936132983
                        print('=> Result:', V1, M1,'=', result, C1)
                elif C1 == 'inch':
                        result = V1 * 39.37007874
                        print('=> Result:', V1, M1,'=', result, C1)
                else:
                        print('** Error! Please Input Precise Conversion')

        elif M1 == 'centimeter':
                if C1 == 'kilometer':
                        result = V1 * 0.00001
                        print('=> Result:', V1, M1,'=', result, C1)
                elif C1 == 'meter':
                        result = V1 * 0.01
                        print('=> Result:', V1, M1,'=', result, C1)
                elif C1 == 'mile':
                        result = V1 * 0.0000062137
                        print('=> Result:', V1, M1,'=', result, C1)
                elif C1 == 'yard':
                        result = V1 * 0.010936133
                        print('=> Result:', V1, M1,'=', result, C1)
                elif C1 == 'inch':
                        result = V1 * 0.3937007874
                        print('=> Result:', V1, M1,'=', result, C1)
                else:
                        print('** Error! Please Input Precise Conversion')

        elif M1 == 'mile':
                if C1 == 'kilometer':
                        result = V1 * 1.60935
                        print('=> Result:', V1, M1,'=', result, C1)
                elif C1 == 'meter':
                        result = V1 * 1609.35
                        print('=> Result:', V1, M1,'=', result, C1)
                elif C1 == 'centimeter':
                        result = V1 * 160935
                        print('=> Result:', V1, M1,'=', result, C1)
                elif C1 == 'yard':
                        result = V1 * 1760.0065617
                        print('=> Result:', V1, M1,'=', result, C1)
                elif C1 == 'inch':
                        result = V1 * 63360.23622
                        print('=> Result:', V1, M1,'=', result, C1)
                else:
                        print('** Error! Please Input Precise Conversion')

        elif M1 == 'yard':
                if C1 == 'kilometer':
                        result = V1 * 0.0009144
                        print('=> Result:', V1, M1,'=', result, C1)
                elif C1 == 'meter':
                        result = V1 * 0.9144
                        print('=> Result:', V1, M1,'=', result, C1)
                elif C1 == 'centimeter':
                        result = V1 * 91.44
                        print('=> Result:', V1, M1,'=', result, C1)
                elif C1 == 'mile':
                        result = V1 * 0.0005681797
                        print('=> Result:', V1, M1,'=', result, C1)
                elif C1 == 'inch':
                        result = V1 * 36
                        print('=> Result:', V1, M1,'=', result, C1)
                else:
                        print('** Error! Please Input Precise Conversion')

        elif M1 == 'inch':
                if C1 == 'kilometer':
                        result = V1 * 0.0000254
                        print('=> Result:', V1, M1,'=', result, C1)
                elif C1 == 'meter':
                        result = V1 * 0.0254
                        print('=> Result:', V1, M1,'=', result, C1)
                elif C1 == 'centimeter':
                        result = V1 * 2.54
                        print('=> Result:', V1, M1,'=', result, C1)
                elif C1 == 'mile':
                        result = V1 * 0.0000157828
                        print('=> Result:', V1, M1,'=', result, C1)
                elif C1 == 'yard':
                        result = V1 * 0.0277777778
                        print('=> Result:', V1, M1,'=', result, C1)
                else:
                        print('** Error! Please Input Precise Conversion')

        else:
                print('** Error! Please Input Precise Measurement')

