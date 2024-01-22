import mymath


while True:
    menu = input("1) ºF -> ºC   2) ºC -> ºF   3) 소수 판별하기 4)구간별 소수 구하기 5) 종료 ")
    if menu == '1':
        Fahrenheit = float(input('INPUT Fahrenheit : '))
        Calculate_Celsius = mymath.fahrenheit_to_celsius(Fahrenheit)
        print(f'화씨 : {Fahrenheit}ºF 섭씨 : {Calculate_Celsius:.4f}ºC')
    elif menu == '2':
        Celsius = float(input('INPUT Celsius : '))
        Calculate_Fahrenheit = mymath.celsius_to_fahrenheit(Celsius)
        print(f'섭씨 : {Celsius}ºC 화씨 : {Calculate_Fahrenheit:.4f}ºF')
    elif menu == '3':
        num_3 = int(input("INPUT number : "))
        if mymath.isprime(num_3):
            print(f'{num_3}는 소수 입니다.')
        else:
            print(f'{num_3}는 소수가 아닙니다')
    elif menu == '4':
        start, finish = map(int, input("INPUT 'start finish' : ").split())

        if start > finish:
            start, finish = finish, start
        for number in range(start, finish + 1):
            if mymath.isprime(number):
                 print(number, end=' ')
        print('\n')
    elif menu == "5":
        print("종료")
        break
    else:
        print("INVALID MENU")