import random

class OopsException(Exception):
    pass
numbers = [random.randint(1, 100) for i in range(random.randint(1, 10))]

print(numbers)
try:
    pick = int(input(f"Input index (0 ~ {len(numbers)-1}) : "))
    print(numbers[pick])
    raise OopsException("Oops!!")
except IndexError as err:
    print(f"{err} : Wrong index number ")
except ValueError as err:
    print(f"{err} : Input only number ")
except OopsException as err:
    print(f'Oops {err}')
except Exception:
    print("Error occurs")
else:
    print(f"Program Terminate")