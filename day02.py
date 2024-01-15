n_1st = int(input("First number : "))
n_2nd = int(input("Second number : "))

quotient = n_1st // n_2nd
remainder = n_1st % n_2nd
print(f'몫은 {quotient} 나머지는 {remainder}')
print(f'몫은 {divmod(n_1st,n_2nd)[0]} 나머지는 {divmod(n_1st,n_2nd)[1]}')