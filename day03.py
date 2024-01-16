#prime number
number = int(input("INPUT number : "))
count = 0
i = 1
while i <= number:
    if number % i == 0:
        count += 1
    i += 1

if count == 2:
    print(f'{number} is prime number')
else:
    print(f'{number} is not prime number')
