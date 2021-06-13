#Syntax for lists
animals_list = ['Monkey', 'Lion', 'Tiger']

#Syntax for tuple
animals_tuple = ('Monkey', 'Lion', 'Tiger')

#Indexing for at få bestemt element
animalList = animals_list[0]
animalTuple = animals_tuple[0]

#Slicing
newAnimalsList = animals_list[1:]
newAnimalTuple = animals_tuple[1:]

#Ændre element i list
animals_list[1] = 'Human'

#Tilføje og fjerne fra list
animals_list.append('Flamingo')
animals_list.pop(2) #Hvis man fjerner index, fjerner den sidste position
animals_list.remove('Monkey')
