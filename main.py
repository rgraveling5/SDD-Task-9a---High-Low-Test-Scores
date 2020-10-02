"""
Program Title

A Programmer
01/01/1970

A brief description of what the program does
"""
names = []
scores = []

for x in range(3):
  names.append(input("Name: "))
  scores.append(input("Scores: "))

maximum = scores[0]
for x in range(len(scores)):
    if maximum > scores[x]:
        maximum = scores[x]
        
print("The highest score is " + str(maximum))
print()

minimum = scores[0]
for x in range(len(scores)):
    if minimum < scores[x]:
        minimum = scores[x]
print("The highest score is " + str(minimum) + "by" )
print()

