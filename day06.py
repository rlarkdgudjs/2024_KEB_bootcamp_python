import random

numbers = [random.randint(1, 100) for i in range(random.randint(1, 10))]

print(numbers)
try:
    pick = int(input(f"Input index (0 ~ {len(numbers)-1}) : "))
    print(numbers[pick])
except IndexError as err:
    print(f"{err} : Wrong index number ")
except ValueError as err:
    print(f"{err} : Input only number ")
except Exception:
    print("Error occurs")
