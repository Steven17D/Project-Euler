""" #22 Names scores"""

data = sorted(map(lambda x: x.replace('"',"").replace('"',""), open("p022_names.txt","r").read().split(',')))
totalScore = 0

def nameScore(name):
    score = 0
    for char in name:
        score += ord(char) - ord('A') + 1
    return score

for n in range(len(data)):
    totalScore += (n+1) * nameScore(data[n])

print totalScore

