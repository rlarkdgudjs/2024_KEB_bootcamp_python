#9.1
def good():
    return ['Harry', 'Ron', 'Hermione']
#9.2
def get_odds(first=1, end=10, step=2):
    n = first
    while n < end:
        yield n
        n += step

c = 1
for i in get_odds():
    if c == 3:
        print(i)
    c += 1
#9.3
def test(func):
    def S_E_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
    return S_E_func
@test
def goodjob():
    print("hello")

goodjob()
#9.4
class OopsException(Exception):
    pass
try:
    raise OopsException('panic')
except OopsException as exc :
    print("Caught an Oops")



