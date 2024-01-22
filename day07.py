class FlyingBehavior():
    def fly(self):
        return f'{self.name}이(가) 공중날기를 사용합니다.'
class JetPack(FlyingBehavior):
    def fly(self):
        return f'제트팩을 사용합니다.'

class NoFly(FlyingBehavior):
    def fly(self):
        return f'공중날기를 사용할 수 없습니다.'
class FlywWing(FlyingBehavior):
    def fly(self):
        return f'공중날기를 사용합니다'

class Pikachu:
    def __init__(self, name, Hp):
        self.name = name
        self.Hp = Hp
        self.fly_behavior = NoFly()  # composition


p1 = Pikachu("피카츄",35)
print(p1.fly_behavior.fly())