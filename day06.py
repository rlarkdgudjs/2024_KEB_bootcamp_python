class Pokemon:
    def __init__(self, name):
        self.name = name

    def attack(self, target):
        print(f'{self.name}이(가) {target.name}을(를) 공격!')


class Pikachu(Pokemon):  # is-a
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

    def attack(self, target):
        print(f'{self.name}이(가) {target.name}을(를) 향해 전광석화!')

    def type_info(self):
        print(f"{self.type} 타입 포켓몬")


class Squirtle(Pokemon):
    pass


class Agumon:
    pass


p1 = Pikachu("피카츄", "전기")
p2 = Squirtle('꼬부기')
p1.attack(p2)
p2.attack(p1)
p1.type_info()
print(p1.name, p1.type)
print(issubclass(Pikachu, Pokemon))
print(issubclass(Agumon, Pokemon))
