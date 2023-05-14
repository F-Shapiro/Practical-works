from itertools import permutations
numbersStr = '1234567890'
simbolsStr = '!@#№$%^&*'
lettersStr = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz'
class PasswordGenerate:
    password_of_numbers = ''
    password_of_simblos = ''
    password_of_letters = ''
    def writeToAttributes(self, nsl):
        for i in nsl:
            if i.lower() in numbersStr:
                self.password_of_numbers += i
            elif i.lower() in simbolsStr:
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
        return list(permutations(self.password_of_numbers)), list(permutations(self.password_of_simblos)), list(permutations(self.password_of_letters))

myClass = PasswordGenerate()
myClass.writeToAttributes(input('Press input string of password: '))
print(myClass.generateCombinationNumbers(),
    myClass.generateCombinationSimbols(),
    myClass.generateCombinationLetters(),
    myClass.generateAllCombination()
)
