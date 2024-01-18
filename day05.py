# prime number
def isprime(n) -> bool:
    """
    매개변수로 받은 수가 소수인지 여부를 boolean으로 리턴
    :param n: 판정할 매개변수
    :return: 소수면 True
    """
    if n < 2:
        return False
    else:
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True


start, finish = map(int, input("INPUT 'start finish' : ").split())

if start > finish: # start, finish = min(start, finish), max(start, finish)
    start, finish = finish, start
for number in range(start, finish + 1):
    if isprime(number):
        print(number, end=' ')
