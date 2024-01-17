
while True:
    menu = input("1) ºF -> ºC   2) ºC -> ºF   3) 소수 판별하기 4)구간별 소수 구하기 5) 종료 ")
    if menu == '1':
        Fahrenheit = float(input('INPUT Fahrenheit : '))
        Calculate_Celsius = (Fahrenheit - 32) * 5 / 9
        print(f'화씨 : {Fahrenheit}ºF 섭씨 : {Calculate_Celsius:.4f}ºC')
    elif menu == '2':
        Celsius = float(input('INPUT Celsius : '))
        Calculate_Fahrenheit = (Celsius * 9 / 5) + 32
        print(f'섭씨 : {Celsius}ºC 화씨 : {Calculate_Fahrenheit:.4f}ºF')
    elif menu == '3':
        num_3 = int(input("INPUT number : "))
        is_prime = True
        if num_3 < 2:
            is_prime = False
            print(f'{num_3}는 소수가 아닙니다')
        else:
            for i in range(2, num_3):
                if num_3 % i == 0:
                    is_prime = False
                    print(f'{num_3}는 소수가 아닙니다')
                    break
            if is_prime:
                print(f'{num_3}는 소수 입니다.')
    elif menu == '4':
        start, finish = map(int, input("INPUT 'start finish' : ").split())

        if start > finish:
            start, finish = finish, start
        for number in range(start, finish + 1):
            is_prime = True
            if number < 2:
                pass
            else:
                for j in range(2, number):
                    if number % j == 0:
                        is_prime = False
                        break
                if is_prime:
                    print(number, end=' ')
        print('\n')
    elif menu == "5":
        print("종료")
        break
    else:
        print("INVALID MENU")
# 개선점 - 소수찾기 성능, 중복코드
