import random
alcs_foods = {"위스키": "과일", "와인": "치즈", "소주": "삼겹살", "고량주": "양꼬치"}


# del alcs_foods['위스키']
# alcs_foods['사케'] = '회'
sub_alcs_foods = {"사케": "회", "위스키": "초콜릿"}
alcs_foods.update(sub_alcs_foods)
# alc = input(drinks_foods.keys())
alcs_foods_keys = list(alcs_foods)

while True:
    select_alc = input(f'주류를 골라주세요. \n1) {alcs_foods_keys[0]} 2) {alcs_foods_keys[1]}'
                       f' 3) {alcs_foods_keys[2]} 4) {alcs_foods_keys[3]} 5) 랜덤선택 6) 종료 : ')
    if select_alc == '1':
        print(f'{alcs_foods_keys[0]}에 어울리는 안주는 {alcs_foods[alcs_foods_keys[0]]} 입니다.')
    elif select_alc == '2':
        print(f'{alcs_foods_keys[1]}에 어울리는 안주는 {alcs_foods[alcs_foods_keys[1]]} 입니다.')
    elif select_alc == '3':
        print(f'{alcs_foods_keys[2]}에 어울리는 안주는 {alcs_foods[alcs_foods_keys[2]]} 입니다.')
    elif select_alc == '4':
        print(f'{alcs_foods_keys[3]}에 어울리는 안주는 {alcs_foods[alcs_foods_keys[3]]} 입니다.')
    elif select_alc == '5':
        random_alc = random.choice(alcs_foods_keys)
        print(f'{random_alc}에 어울리는 안주는 {alcs_foods[random_alc]} 입니다.')
    elif select_alc == '6':
        print(f'메뉴를 종료합니다')
        break