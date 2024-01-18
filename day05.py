# univ = 'inha university'
# count_letter = {letter: univ.count(letter) for letter in univ} # dictionary comprehension
# print(count_letter)

univ = 'inha university'
count_letter = dict()
for letter in univ:
    count_letter[letter] = univ.count(letter)
print(count_letter)