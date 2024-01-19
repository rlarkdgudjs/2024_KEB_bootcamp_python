class FlyingMixin:
    def fly(self):
        return f'{self.name}이(가) 비행중입니다.'


class SwimmingMixin:
    def swim(self):
        return f'{self.name}이(가) 수영중입니다.'


class Pokemon:
    def __init__(self,name):
        self.name = name


class Charizard(Pokemon, FlyingMixin):
    pass


class Gyarados(Pokemon, SwimmingMixin, FlyingMixin):
    pass

g1 = Gyarados("갸랴도스")
c1 = Charizard("리자몽")

print(g1.fly())
print(g1.swim())
print(c1.fly())
