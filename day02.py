letter = input('INPUT alphabet : ')
# vowels = {'a','e','i','o','u'} #set
vowels = 'aeiou'
if letter in vowels:
    print(f'{letter} is a vowel')
else:
    print(f'{letter} is a consonant')