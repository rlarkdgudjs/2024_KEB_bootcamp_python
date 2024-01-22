class FlyingBehavior():
    def fly(self):
        return f'{self.__name}이(가) 공중날기를 사용합니다.'
class JetPack(FlyingBehavior):
    def fly(self):
        return f'제트팩을 사용합니다.'

class NoFly(FlyingBehavior):
    def fly(self):
        return f'공중날기를 사용할 수 없습니다.'
class FlywWing(FlyingBehavior):
    def fly(self):
        return f'공중날기를 사용합니다'
class SwimmingBehavior():
    def swim(self):
        return f'{self.__name}이(가) 파도타기를 사용합니다.'

class Pokemon:
    def __init__(self, name, Hp, fly):
        self.__name = name
        self.Hp = Hp
        self.fly_behavior = fly # aggregation (has-a)
    def set_fly_behavior(self, fly):
        self.fly_behavior = fly
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

class Charizard(Pokemon):
    pass

class Gyarados(Pokemon):
    pass

class Pikachu(Pokemon):
    pass

nofly = NoFly()
wings = FlywWing()

p1 = Pikachu("피카츄", 50, nofly)
g1 = Gyarados("갸랴도스", 100, wings)
c1 = Charizard("리자몽", 120, wings)
print(g1)
print(c1)
print(g1 + c1)
print(g1.fly_behavior.fly())
print(p1.fly_behavior.fly())
p1.set_fly_behavior(JetPack())
print(p1.fly_behavior.fly())
