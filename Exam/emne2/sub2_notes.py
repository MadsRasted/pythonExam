#OOP

class Dog:

    species = 'This is a dog'

#__init__ = constructor
#Definerer variabler inden i som skal være anderledes fra object til object
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Her laves en metode med f String metode, som fungerer som en slags toString()
    def description(self):
        return f'{self.species}, its called {self.name} and it is {self.age} years old'

#Samme funktion som ovenstående, men laver som dunder method. Mere pythonic way at gøre det
#Gør at jeg kan printe objektet jeg laver og få en string ud.
    def __str__(self):
        return f'{self.species}, its called {self.name} and it is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'

#___________________________Child classes
class Labrador(Dog):
    def speak(self, sound = 'woof barf'):
        return f"{self.name} says {sound}"

class Poodle(Dog):
    pass

#Her opretter vi objecter af dog og underklasser

pluto = Dog('Pluto', 12)
vaks = Labrador('Vaks', 4)
nuser = Poodle('Nuser', 7)

print(pluto)
print(vaks)
print(nuser)

print(pluto.speak('woof woof'))
print(vaks.speak())

print(isinstance(vaks, Dog))

dogList = [pluto, vaks, nuser]
for x in dogList:
    print(x.__str__())

print("________________________________________________________________________________")

class PrivatePerson:
#Har 2 private variabler
    def __init__(self, name, nickname):
        self.__name = name
        self.__nickname = nickname

    def __add__(self, other):
        return f'{self.__name } and {other.__name}'

    @property
    def name(self):
        return self.__name

    @property
    def nickname(self):
        return self.__nickname

    @name.setter
    def name(self, name):
        self.__name = name

    @nickname.setter
    def nickname(self, nickname):
        self.__nickname = nickname

    def who(self):
        print('name : ', self.__name)
        print('nickname : ', self.__nickname)


p = PrivatePerson("Mads", "nørd")
p2 = PrivatePerson("Nick", "freak")
print(p.name)
print(p.nickname)

print(p + p2)

#p.who()

