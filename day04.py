import copy
# subjects = ["a", "b", "13"]
subjects = ["a", ["b", "13"], "d"]
a = subjects
b = subjects.copy()
c = list(a)
d = subjects[:]
e = copy.deepcopy(subjects)

print(subjects, a, b, c, d, e)
subjects[1][1] = "x"
print(subjects, a, b, c, d, e) # 리스트 원소중에 mutable 한값이 바뀌면 shallow copy한 값들도 같이 바뀜
# pythontutor.com


