menu = input("1) F -> C   2) C -> F   3) Quit ")
if menu == '1':
    Fahrenheit = float(input('INPUT Fahrenheit : '))
    Calculate_Celsius = (Fahrenheit - 32) * 5 / 9
    print(f'화씨 : {Fahrenheit}F 섭씨 : {Calculate_Celsius:.4f}C')
elif menu == '2':
    Celsius = float(input('INPUT Celsius : '))
    Calculate_Fahrenheit = (Celsius * 9 / 5) + 32
    print(f'섭씨 : {Celsius}C 화씨 : {Calculate_Fahrenheit:.4f}F')