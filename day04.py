# prime number
start, finish = map(int, input("INPUT 'start finish' : ").split())

if start > finish:
    start, finish = finish, start

for number in range(start, finish + 1):
    is_prime = True

    if number < 2:
        continue
    else:
        i = 2
        while i*i <= number:
            if number % i == 0:
                is_prime = False
                break
            i += 1
            # print(i, end=' ')
        # for j in range(2, number):
        #     if number % j == 0:
        #         is_prime = False
        #         break
        if is_prime:
            # pass
            print(number, end=' ')

