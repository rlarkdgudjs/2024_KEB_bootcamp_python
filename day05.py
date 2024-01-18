# 하드리셋으로 푸쉬 이전 내용들 사라졌음

# def squares(n):
#     return n*n

even_numbers = [i for i in range(51) if i % 2 == 0]
print(even_numbers)
# print(tuple(map(squares, even_numbers)))
# print(tuple(map(lambda x : x**2, even_numbers)))
z = lambda x: x*x
print(list(map(z,even_numbers)))