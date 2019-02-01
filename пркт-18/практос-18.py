from itertools import permutations
from os.path import dirname
from time import time
alphabet = ''
with open(dirname(__file__) + '/алфавит.txt', 'r') as myFile:
    alphabet = myFile.read()
def unlocked(unlocke_str, password):
    if len(unlocke_str) == len(password):
        if unlocke_str == password:
            total = True
            return total
    else:
        for i in alphabet:
            if unlocked(unlocke_str+i, password) == True:
                total = True
                return total
        total = False
        return total
numbers_str = '1234567890'
simbols_str = '!@#№$%^&*'
letters_str = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz'
class PasswordGenerate:
    password_of_numbers = ''
    password_of_simblos = ''
    password_of_letters = ''
    def setAttr(self, nsl):
        for i in nsl:
            if i.lower() in numbers_str:
                self.password_of_numbers += i
            elif i.lower() in simbols_str:
                self.password_of_simblos += i
            else:
                self.password_of_letters += i

    def generateCombinationNumbers(self):
        return list(permutations(self.password_of_numbers))
    
    def generateCombinationSimbols(self):
        return list(permutations(self.password_of_simblos))

    def generateCombinationLetters(self):
        return list(permutations(self.password_of_letters))

    def generateAllCombination(self):
        return (list(permutations(self.password_of_numbers)),
            list(permutations(self.password_of_simblos)),
            list(permutations(self.password_of_letters))
            )

class Analysis(PasswordGenerate):
    memory = 0
    def measureRateSelectionPassword(self, password, fun):
        start = time()
        fun('', password)
        self.memory = round((time() - start),3)
        return self.memory
    
    def __eq__(self, other):
        if not isinstance(other, Analysis):
            return False
        return self.memory == other.memory
    
    def __ne__(self, other):
        if not isinstance(other, Analysis):
            return False
        return self.memory != other.memory

myClass2 = Analysis()
myClass3 = Analysis()
myClass2.measureRateSelectionPassword('хай', unlocked)
myClass3.measureRateSelectionPassword('hi', unlocked)
print(myClass2 == myClass3, myClass2.memory, myClass3.memory)
print(myClass2 == 4)
print(myClass2 != myClass3, myClass2.memory, myClass3.memory)
print(myClass2 != 3)