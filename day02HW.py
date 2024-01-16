
while True:
    menu = input("1) ºF -> ºC   2) ºC -> ºF   3) Quit ")
    if menu == '1':
        Fahrenheit = float(input('INPUT Fahrenheit : '))
        Calculate_Celsius = (Fahrenheit - 32) * 5 / 9
        print(f'화씨 : {Fahrenheit}ºF 섭씨 : {Calculate_Celsius:.4f}ºC')
    elif menu == '2':
        Celsius = float(input('INPUT Celsius : '))
        Calculate_Fahrenheit = (Celsius * 9 / 5) + 32
        print(f'섭씨 : {Celsius}ºC 화씨 : {Calculate_Fahrenheit:.4f}ºF')
    elif menu == '3':
        break
print("종료")