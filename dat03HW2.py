# 1
numbers=[]
for i in range(3,-1,-1):
    numbers.append(i)
print(numbers)

# 2
guess_me = 7
number = 1
while True:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it")
        break
    elif number > guess_me:
        print("oops")
        break
    number += 1

# 3
guess_me = 5
for number in range(10):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it")
        break
    elif number > guess_me:
        print("oops")
        break
    number += 1