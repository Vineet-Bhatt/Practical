fh = open("poem.txt")

data = fh.read()

upperCount = 0
lowerCount = 0
consonantCount = 0
vowelCount = 0
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

for i in data:
    if i.isupper():
        upperCount += 1
    if i.islower():
        lowerCount += 1
    if i.lower() in vowels:
        vowelCount += 1
    if i.lower() in consonants:
        consonantCount += 1

print("Number of uppercase letters : ",upperCount)
print("Number of lowercase letters : ",lowerCount)
print("Number of vowels : ",vowelCount)
print("Number of consonant : ",consonantCount)