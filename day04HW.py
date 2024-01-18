# 8.1
e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}
print(e2f)
#8.2
print(e2f.get("walrus"))
#8.3
e2f_list = list(e2f.items())
f2e_list = e2f_list[::-1]
f2e = dict(f2e_list)
print(f2e)
#8.4
for en,fr in e2f.items():
    if "chien" in fr:
        print(en)
#8.5
print(e2f.keys())
#8.6
a = ("cats", "Henri"), ("octopi", "Grumpy"), ("emus", "Lucy")
life = {"animals": dict(a), 'plants': dict(), "other": dict()}
print(life)
#8.7
print(life.keys())
#8.8
print(life['animals'].keys())
#8.9
print(life['animals']['cats'])
#8.10
squares = {i: i*i for i in range(10)}
print(squares)