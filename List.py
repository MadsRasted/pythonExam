#List
animalList = ['Hamster', 'Tiger', 'Gnu']
carList = ['Volvo', 'Jeep']
largeAnimal = ('Elefant', 'Giraf') #tuple
print(animalList)

#Lægger to lister sammen til én
print(animalList + carList)

#Indsætter object til sidst i listen
animalList.append('Bumblebee')
print(animalList)

#Indsætter object på specifikt index
animalList.insert(0, 'Ape')
print(animalList)

#Føjer en ny liste/tuple
animalList.extend(largeAnimal)
print(animalList)

#Fjerner et index
animalList.pop(1) #If no index, remove last
print(animalList)

#Sletter et index
del animalList[1]
print(animalList)

#Clearer liste
animalList.clear()
print(animalList)


#Dictionary

superliga = {
    'FCK': 'København',
    'BIF': 'Brøndby',
    'FCN': 'Farum',
    'FCM': 'Midt Jylland',
}
print(superliga)
print(superliga['FCK'])

#Dictionary til person
person = {}
type = (person)

person['fName'] = 'Mads'
person['lName'] = 'Rasted'
person['age'] = 22
person['friends'] = ['Jonas', 'Nick', 'Max']
person['pets'] = {'Dog': 'Julius', 'Fish': 'Morten'}

print(person)
print(person['friends'][0:])
print(person['pets']['Dog'])

