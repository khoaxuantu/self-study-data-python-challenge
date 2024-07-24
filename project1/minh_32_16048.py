# Temp converter
class TempConverter:
    def __init__(self, in_num) -> None:
        self.in_num = in_num

class CelsiusTemp(TempConverter):
    def __init__(self, in_num) -> None:
        super().__init__(in_num)

    def celsiusToKelvin(self) -> float:
        self.in_num += 273.15
        return self.in_num
    
    def celsiusToFarh(self) -> float:
        self.in_num = self.in_num*(9/5) + 32
        return self.in_num

class FahenritTemp(TempConverter):
    def __init__(self, in_num) -> None:
        super().__init__(in_num)

    def farhenToCelsius(self)-> float:
        self.in_num = (self.in_num-32)*(5/9)
        return self.in_num
    
    def farhenToKelvin(self) -> float:
        self.in_num = (self.in_num+459.67)*(5/9)
        return self.in_num

class KelvinTemp(TempConverter):
    def __init__(self, in_num) -> None:
        super().__init__(in_num)

    def kelvinToCelsius(self) -> float:
        self.in_num -= 273.15
        return self.in_num
    
    def kelvinToFarh(self) -> float:
        self.in_num = (self.in_num*(9/5)) - 459.67
        return self.in_num
    
# Weight converter:
class WeightConverter:
    def __init__(self, in_num) -> None:
        self.in_num = in_num

class PoundMeasure(WeightConverter):
    def __init__(self, in_num) -> None:
        super().__init__(in_num)

    def poundToKg(self) -> float:
        return self.in_num*0.453592
    def poundToKg(in_num) -> float:
        return in_num*0.453592
    
    def poundToOz(self) -> float:
        return self.in_num/16
    def poundToOz(in_num) -> float:
        return in_num/16
    
    def kgToPound(self) -> float:
        return self.in_num*(1/0.453592)
    
    def ozToPound(self) -> float:
        return self.in_num*16

class KilogramMeasure(WeightConverter):
    def __init__(self, in_num) -> None:
        super().__init__(in_num)

    def kilogrToGram(self)->float:
        return self.in_num*1000
    
    def kilogrToMiligram(self)->float:
        return self.in_num*1e6
    
    def kilogrToMetricTon(self)->float:
        return self.in_num*0.001
    
    def kiloToPound(self) -> float:
        return PoundMeasure(self.in_num).kgToPound()
    
    def kiloToLongTon(self)->float:
        pound_metric = PoundMeasure(self.in_num).kgToPound()
        return pound_metric/2240
    
    def kiloToShortTon(self)->float:
        pound_metric = PoundMeasure(self.in_num).kgToPound()
        return pound_metric/2000
    
    def kiloToOz(self) -> float:
        pound_obj = PoundMeasure(self.in_num)
        pound_metric = pound_obj.kgToPound()
        return pound_obj.poundToOz(pound_metric)
    
    def kiloToCarrat(self) -> float:
        return self.in_num*5000
    
    def kiloToAtomicUnit(self)-> float:
        return self.in_num*(1/1.66053907*10E-27)
    
class GramMeasure(KilogramMeasure):
    def __init__(self, in_num) -> None:
        super().__init__(in_num)
        self.in_num = in_num*0.001

class MilligramMeasure(KilogramMeasure):
    def __init__(self, in_num) -> None:
        super().__init__(in_num)
        self.in_num = in_num*0.000001
    
class MetricTonMeasure(KilogramMeasure):
    def __init__(self, in_num) -> None:
        super().__init__(in_num)
        self.in_num = in_num*1000 #convert directly into kilogram

class LongTonMeasure(KilogramMeasure):
    def __init__(self, in_num) -> None:
        super().__init__(in_num)
        #convert directly from long ton -> kilogram
        pound_convert = PoundMeasure(self.in_num)
        pound_metric = pound_convert.in_num*2240
        self.in_num = pound_convert.poundToKg(pound_metric) 

class ShortTonMeasure(KilogramMeasure):
    def __init__(self, in_num) -> None:
        super().__init__(in_num)
            #convert directly from short ton -> kilogram
        pound_convert = PoundMeasure(self.in_num)
        pound_metric = pound_convert.in_num*2000
        self.in_num = pound_convert.poundToKg(pound_metric) 

class Pound2Measure(KilogramMeasure):
    def __init__(self, in_num) -> None:
        super().__init__(in_num)
        self.in_num = PoundMeasure(self.in_num).poundToKg(self)

class OzMeasure(KilogramMeasure):
    def __init__(self, in_num) -> None:
        super().__init__(in_num)
        #convert directly from oz -> kilogram
        pound_conveter = PoundMeasure(self.in_num)
        toPound = pound_conveter.ozToPound(self)
        self.in_num = pound_conveter.poundToKg(toPound)

class CarratMeasure(KilogramMeasure):
    def __init__(self, in_num) -> None:
        super().__init__(in_num)
        # convert carrat to kilogram
        self.in_num *= (1/5000)

class AtomicUnitMeasure(KilogramMeasure):
    def __init__(self, in_num) -> None:
        super().__init__(in_num)
        # convert atomic to kilo:
        self.in_num *= 1.66053907*10E-27

# Function hien thi cac lua chon
def tempConverterModule(module_no) -> None:
    print('Chon thang do muon chuyen doi sang: \n4. Celsius \n5.Kelvin \n6.Fahrenheit')
    select_item_2 = int(input())
    while(select_item_2 > 6 or select_item_2 < 4):
        print('Lua chon cua ban khong ton tai, hay lua chon lai')
        select_item_2 = int(input())
    print('Nhap gia tri can chuyen doi: ')
    source_conv = float(input())
    temp_conveter = None
        # Which converter is used?
    if (module_no == 1):
        temp_conveter = CelsiusTemp(source_conv)
        # For each destination items:
        if (select_item_2 == 4):
            res = temp_conveter.in_num
            print(f'{source_conv} Celsius degree = {res} Celsius degree')
        elif select_item_2 == 5:
            res = temp_conveter.celsiusToKelvin()
            print(f'{source_conv} Celsius degree = {res} Kelvin degree')
        else:
            res = temp_conveter.celsiusToFarh()
            print(f'{source_conv} Celsius degree = {res} Fahrenheit degree')
    elif (module_no == 2):
        temp_conveter = KelvinTemp(source_conv)
        # For each destination items:
        if (select_item_2 == 4):
            res = temp_conveter.kelvinToCelsius()
            print(f'{source_conv} Kelvin degree = {res} Celsius degree')
        elif (select_item_2 == 5):
            res = temp_conveter.in_num
            print(f'{source_conv} Kelvin degree = {res} Kelvin degree')
        else:
            res = temp_conveter.kelvinToFarh()
            print(f'{source_conv} Kelvin degree = {res} Fahrenheit degree')
    else:
        temp_conveter = FahenritTemp(source_conv)
        # For each destination items:
        if (select_item_2 == 4):
            res = temp_conveter.farhenToCelsius()
            print(f'{source_conv} Fahrenheit degree = {res} Celsius degree')
        elif (select_item_2 == 5):
            res = temp_conveter.farhenToKelvin()
            print(f'{source_conv} Fahrenheit degree = {res} Kelvin degree')
        else:
            res = temp_conveter.in_num
            print(f'WE GOT {res} Fahrenheit degree')
        
def tempConvertMenu() -> None:
    in_subcate_1 = True
    while(in_subcate_1):
        print('Chon thang do can chuyen doi (neu muon thoat, nhan so bat ky ngoai cac lua chon o day): \n1. Celsius \n2.Kelvin \n3.Fahrenheit')
        select_item = int(input())
        if (select_item == 1):
            tempConverterModule(select_item)
        elif (select_item == 2):
            tempConverterModule(select_item)
        elif (select_item == 3):
            tempConverterModule(select_item)
        else:
            print('Khong co lua chon thang do thich hop voi lua chon cua ban, hay chon lai lua chon o tren')
            print('Neu ban muon chuyen doi muc khac, hay nhan x: ')
            choose_item = input()
            if (choose_item == 'x'):
                in_subcate_1 = False
            else: continue

def weightConveterModule(module_no):
    print('Chon thang do muon chuyen doi sang: ')
    print('\n8. Kilogram \n9. Gram \n10. Milligram \n11. Metric Ton \n12. Long Ton \n13. Short Ton \n14. Carrat')
    select_item_3 = int(input())
    while(select_item_3 > 14 or select_item_3 < 8):
        print('Lua chon cua ban khong ton tai, hay lua chon lai')
        select_item_3 = int(input())
    print('Nhap gia tri can chuyen doi: ')
    source_conv = float(input())
    while source_conv < 0:
        print("Nhap lai gia tri khoi luong ban dau, khong duoc am")
        source_conv = float(input())
    weight_converter = None
    # Which weight conveter is used?
    if (module_no == 1):
        weight_converter = KilogramMeasure(source_conv)
        if (select_item_3 == 8):
            print(f'We have {source_conv} Kilogram')
        elif (select_item_3 == 9):
            res = weight_converter.kilogrToGram()
            print(f'{source_conv} Kilogram = {res} Gram')
        elif (select_item_3 == 10):
            res = weight_converter.kilogrToMiligram()
            print(f'{source_conv} Kilogram = {res} Milligram')
        elif (select_item_3 == 11):
            res = weight_converter.kilogrToMetricTon()
            print(f'{source_conv} Kilogram = {res} Metric Ton')
        elif (select_item_3 == 12):
            res = weight_converter.kiloToLongTon()
            print(f'{source_conv} Kilogram = {res} Long Ton')
        elif (select_item_3 == 13):
            res = weight_converter.kiloToShortTon()
            print(f'{source_conv} Kilogram = {res} Short Ton')
        else:
            res = weight_converter.kiloToCarrat()
            print(f'{source_conv} Kilogram = {res} Carrat')
    elif (module_no == 2):
        weight_converter = GramMeasure(source_conv)
        if (select_item_3 == 8):
            res = weight_converter.in_num
            print(f'{source_conv} gram = {res} kilogram')
        elif (select_item_3 == 9):
            print(f'We have {source_conv} gram')
        elif (select_item_3 == 10):
            res = weight_converter.kilogrToMiligram()
            print(f'{source_conv} gram = {res} milligram')
        elif (select_item_3 == 11):
            res = weight_converter.kilogrToMetricTon()
            print(f'{source_conv} gram = {res} Metric Ton')
        elif (select_item_3 == 12):
            res = weight_converter.kiloToLongTon()
            print(f'{source_conv} gram = {res} Long Ton')
        elif (select_item_3 == 13):
            res = weight_converter.kiloToShortTon()
            print(f'{source_conv} gram = {res} Short Ton')
        else:
            res = weight_converter.kiloToCarrat()
            print(f'{source_conv} gram = {res} Carrat')
    elif (module_no == 3):
        weight_converter = MilligramMeasure(source_conv)
        if (select_item_3 == 8):
            res = weight_converter.in_num
            print(f'{source_conv} milligram = {res} kilogram')
        elif (select_item_3 == 9):
            res = weight_converter.kilogrToGram()
            print(f'{source_conv} milligram = {res} gram')
        elif (select_item_3 == 10):
            print(f'We have {source_conv} milligram')
        elif (select_item_3 == 11):
            res = weight_converter.kilogrToMetricTon()
            print(f'{source_conv} milligram = {res} Metric Ton')
        elif (select_item_3 == 12):
            res = weight_converter.kiloToLongTon()
            print(f'{source_conv} milligram = {res} Long Ton')
        elif (select_item_3 == 13):
            res = weight_converter.kiloToShortTon()
            print(f'{source_conv} milligram = {res} Short Ton')
        else:
            res = weight_converter.kiloToCarrat()
            print(f'{source_conv} milligram = {res} Carrat')
    elif (module_no == 4):
        weight_converter = MetricTonMeasure(source_conv)
        if (select_item_3 == 8):
            res = weight_converter.in_num
            print(f'{source_conv} Metric Ton = {res} kilogram')
        elif (select_item_3 == 9):
            res = weight_converter.kilogrToGram()
            print(f'{source_conv} Metric Ton = {res} gram')
        elif (select_item_3 == 10):
            res = weight_converter.kilogrToMiligram()
            print(f'{source_conv} Metric Ton = {res} milligram')
        elif (select_item_3 == 11):
            print(f'We have {source_conv} Metric Ton')
        elif (select_item_3 == 12):
            res = weight_converter.kiloToLongTon()
            print(f'{source_conv} Metric Ton = {res} Long Ton')
        elif (select_item_3 == 13):
            res = weight_converter.kiloToShortTon()
            print(f'{source_conv} Metric Ton = {res} Short Ton')
        else:
            res = weight_converter.kiloToCarrat()
            print(f'{source_conv} Metric Ton = {res} Carrat')
    elif (module_no == 5):
        weight_converter = LongTonMeasure(source_conv)
        if (select_item_3 == 8):
            res = weight_converter.in_num
            print(f'{source_conv} Long Ton = {res} kilogram')
        elif (select_item_3 == 9):
            res = weight_converter.kilogrToGram()
            print(f'{source_conv} Long Ton = {res} gram')
        elif (select_item_3 ==10) :
            res = weight_converter.kilogrToMiligram()
            print(f'{source_conv} Long Ton = {res} milligram')
        elif (select_item_3 == 11):
            res = weight_converter.kilogrToMetricTon()
            print(f'{source_conv} Long Ton = {res} Mtric Ton')
        elif (select_item_3 == 12):
            print(f'We have {source_conv} Long Ton')
        elif (select_item_3 == 13):
            res = weight_converter.kiloToShortTon()
            print(f'{source_conv} Long Ton = {res} Short Ton')
        else:
            res = weight_converter.kiloToCarrat()
            print(f'{source_conv} Long Ton = {res} Carrat')
    elif (module_no == 6):
        weight_converter = ShortTonMeasure(source_conv)
        if (select_item_3 == 8):
            res = weight_converter.in_num
            print(f'{source_conv} Short Ton = {res} kilogram')
        elif (select_item_3 == 9):
            res = weight_converter.kilogrToGram()
            print(f'{source_conv} Short Ton = {res} gram')
        elif (select_item_3 == 10):
            res = weight_converter.kilogrToMiligram()
            print(f'{source_conv} Short Ton = {res} milligram')
        elif (select_item_3 == 11):
            res = weight_converter.kilogrToMetricTon()
            print(f'{source_conv} Short Ton = {res} Metric Ton')
        elif (select_item_3 == 12):
            res = weight_converter.kiloToLongTon()
            print(f'{source_conv} Short Ton = {res} Long Ton')
        elif (select_item_3 == 13):
            print(f'We have {source_conv} Short Ton')
        else:
            res = weight_converter.kiloToCarrat()
            print(f'{source_conv} Short Ton = {res} Carrat')
    else:
        weight_converter = CarratMeasure(source_conv)
        if (select_item_3 == 8):
            res = weight_converter.in_num
            print(f'{source_conv} carrat = {res} kilogram')
        elif (select_item_3 == 9):
            res = weight_converter.kilogrToGram()
            print(f'{source_conv} carrat = {res} gram')
        elif (select_item_3 == 10):
            res = weight_converter.kilogrToMiligram()
            print(f'{source_conv} carrat = {res} milligram')
        elif (select_item_3 == 11):
            res = weight_converter.kilogrToMetricTon()
            print(f'{source_conv} carrat = {res} Metric Ton')
        elif (select_item_3 == 12):
            res = weight_converter.kiloToLongTon()
            print(f'{source_conv} carrat = {res} Long Ton')
        elif (select_item_3 == 13):
            res = weight_converter.kiloToShortTon()
            print(f'{source_conv} carrat = {res} Short Ton')
        else:
            print(f'We have {source_conv} carrat')

def weightConvertMenu() -> None:
    in_subcate_2 = True
    while(in_subcate_2):
        print('Chon thang do can chuyen doi (neu muon thoat, nhan so bat ky ngoai cac lua chon o day): ')
        print('\n1. Kilogram \n2. Gram \n3. Milligram \n4. Metric Ton \n5. Long Ton \n6. Short Ton \n7. Carrat')
        select_item = int(input())
        if (select_item == 1):
            weightConveterModule(select_item)
        elif (select_item == 2):
            weightConveterModule(select_item)
        elif (select_item == 3):
            weightConveterModule(select_item)
        elif (select_item == 4):
            weightConveterModule(select_item)
        elif (select_item == 5):
            weightConveterModule(select_item)
        elif (select_item == 6):
            weightConveterModule(select_item)    
        elif (select_item == 7):
            weightConveterModule(select_item)
        else:
            print('Khong co lua chon thang do thich hop voi lua chon cua ban, hay chon lai lua chon o tren')
            print('Neu ban muon chuyen doi muc khac, hay nhan x: ')
            choose_item = input()
            if (choose_item == 'x'):
                in_subcate_2 = False
            else: continue

def startMenu() -> None:
    print('Chao mung den voi chuong trinh chuyen doi don vi!!!')
    while(1):
        print('Chon loai don vi muon chuyen doi: \n1 - Temperature \n2 - Weight')
        select = int(input())
        if (select == 1):
            tempConvertMenu()
        elif (select == 2):
            weightConvertMenu()
        else:
            print('Hien chua co tuy chon khac ngoai 2 tuy chon tren\n Nhan x de thoat, o de tiep tuc:')
            close_sec = input()
            if (close_sec == 'x'):
                break
            else:
                continue


if __name__ == "__main__":
    startMenu()


#Gud job~!