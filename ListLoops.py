#List loops
animalList = ['Hamster', 'Tiger', 'Gnu', 'Lion']

#For loop

#Loop thru
for i in animalList:
    print(i)
print('')

#Loop thru
for i in range(len(animalList)):
    print(animalList[i])

print('')
#Break at position
for i in animalList:
    print(i)
    if i == 'Tiger':
        break
print('')

#___________________________________________________________________________________#
#While loop
i = 0
while i < len(animalList):
    print(animalList[i])
    i += 1
print('')

j = 0
while True:
    print(animalList[j])
    j += 1
    if j == 4:
        break
print('')

#List comprehension
x = 0
[print(x) for x in animalList]
print('')
newAnimalList3 = []
animalList3 = [x for x in animalList]

#Almindeligt for loop til at tage dyr med H i ny liste
newAnimalList = []
for x in animalList:
    if "H" in x:
        newAnimalList.append(x)
print(newAnimalList)


#Samme funktion som for loopet, men lavet som list comprehension, så meget kortere syntax
print('Kun dyr der starter med T')
newAnimalList2 = [x for x in animalList if 'T' in x]
print(newAnimalList2)

print('Upper case')
newAnimalList = [x.upper() for x in animalList]
print(newAnimalList)

print('Nick er dum erstatter alle positions i listen')
newAnimalList = ['Nick er dum' for x in animalList]
print(newAnimalList)

#Replace en position
print("Erstatter hamster med Great ape")
newAnimalList = [x if x != "Hamster" else "Great Ape" for x in animalList]
print(newAnimalList)
