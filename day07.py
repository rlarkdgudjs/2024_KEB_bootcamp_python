class FlyingMixin:
    def fly(self):
        return f'{self.__name}이(가) 비행중입니다.'

class SwimmingMixin:
    def swim(self):
        return f'{self.__name}이(가) 수영중입니다.'

class Pokemon:
    def __init__(self, name, Hp):
        self.__name = name
        self.Hp = Hp

    def attack(self):
        print(f'{self.__name}이(가) 공격!')
    @property
    def name(self):
        print("이름 불러오는중")
        return self.__name
    @name.setter
    def name(self, new_name):
        print('이름 설정중')
        self.__name = new_name

    # input_name = property(get_name, set_name)

    # magic method
    def __str__(self):
        return self.__name + " 입니다."

    def __add__(self, target):
        return f'두 포켓몬 체력의 합은 {self.Hp + target.Hp}입니다'

class Charizard(Pokemon, FlyingMixin):
    pass

class Gyarados(Pokemon, SwimmingMixin, FlyingMixin):
    pass

g1 = Gyarados("갸랴도스", 100)
c1 = Charizard("리자몽", 120)
print(g1)
print(c1)
print(g1 + c1)
