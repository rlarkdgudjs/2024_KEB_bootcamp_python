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
print(e2f.get("chien"))
