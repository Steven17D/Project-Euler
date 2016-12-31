""" #42 Coded triangle numbers"""

data = sorted(map(lambda x: x.replace('"',"").replace('"',""), open("p042_words.txt","r").read().split(',')))

def wordToValue(word):
    word = word.lower()
    sum = 0
    for char in word:
        sum += ord(char) - ord('a') + 1
    return sum

def isTriangleWord(word):
    value = wordToValue(word)
    n = 1.0
    while value >= 0.5 * n * (n + 1):
        if value == 0.5 * n * (n + 1):
            return True
        n += 1.0
    return False

counter = 0

for word in data:
    if isTriangleWord(word):
        counter += 1

print counter

