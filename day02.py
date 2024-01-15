base = int(input('base : '))
exponent = int(input('exp : '))
# f-string
# print(f'밑은 {base}, 시수는 {exponent}, 결과값은 {base**exponent}')
print(f'밑은 {base}, 시수는 {exponent}, 결과값은 {pow(base, exponent)}')

# format function
print('밑은 {0}, 시수는 {1}, 결과값은 {2}'.format(base, exponent, base**exponent))
