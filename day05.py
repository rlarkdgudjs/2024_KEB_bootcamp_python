def my_range(first=0,last=10,step=1):
    number=first
    while number < last:
        yield number
        number += step

r = my_range()
print(r)

for x in r:
    print(x)


# def squares(n):
#     return n*n

even_numbers = [i for i in range(51) if i % 2 == 0]
print(even_numbers)
# print(tuple(map(squares, even_numbers)))
# print(tuple(map(lambda x : x**2, even_numbers)))
z = lambda x: x*x
print(list(map(z,even_numbers)))