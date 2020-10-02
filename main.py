"""
Program Title

A Programmer
01/01/1970

A brief description of what the program does
"""
names = []
scores = []

for x in range(3):
    name = input('Name: ')
    score = int(input('Score: '))

    names.append(name)
    scores.append(score)
print()

maximum = scores[0]
for x in range(len(scores)):
    if scores[x] > maximum:
        maximum = scores[x]
        max_name = names[x]
print('The highest score is ' + str(maximum) + ' scored by ' + max_name)

minimum = scores[0]
for i in range(len(scores)):
    if scores[i] <= minimum:
        minimum = scores[i]
        min_name = names[i]
print('The lowest score is ' + str(minimum) + ' scored by ' + min_name)
print()
