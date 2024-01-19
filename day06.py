def factorial_repetition(n):
    """
    반복문을 이용한 팩토리얼 함수
    :param n: 정수
    :return: 팩토리얼 값
    """
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


def factorial_recursion(n):
    """
    재귀함수를 이용한 팩토리얼 함수
    :param n: 정수
    :return: function, int
    """
    if n == 1:
        return n
    else:
        return n*factorial_repetition(n-1)


print(factorial_repetition(int(input("number : "))))
print(factorial_recursion(int(input("number : "))))
