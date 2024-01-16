# prime number
number = int(input("INPUT number : "))
is_prime = True
i = 2
if number < 2:
    print(f'{number} is not prime number')
else:
    while i < number:
        if number % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(f'{number} is prime number')
    else:
        print(f'{number} is not prime number')

