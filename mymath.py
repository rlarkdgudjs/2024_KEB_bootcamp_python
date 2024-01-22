if __name__ == "__main__":
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


    def fahrenheit_to_celsius(Fahrenheit):
        return (Fahrenheit - 32) * 5 / 9

    def celsius_to_fahrenheit(Celsius):
        return (Celsius * 9 / 5) + 32
else:
    print("mymath is not a main file")