sugang = dict(python="kim", cpp="sung", db="kang")
# print(sugang)
# sugang['datastructure'] = 'kim'
# print(sugang)
# sugang['datastructure'] = 'park'
# print(sugang)
# print(sugang['db'])
# print(sugang.get('db'))
# print(sugang.get('opensource', '존재하지 않습니다'))


for subject, professor in sugang.items():
    print(f'{subject} 과목 담당교수는 {professor}')

for k in sugang:
    print(k)

for k in sugang.keys():
    print(k)

for v in sugang.values():
    print(v)

for v in sugang.items():
    print(v)
