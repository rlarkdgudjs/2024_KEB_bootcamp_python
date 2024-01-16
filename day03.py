# prime number
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


