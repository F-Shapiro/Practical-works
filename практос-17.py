from itertools import permutations
numbersStr = '1234567890'
simbolsStr = '!@#№$%^&*'
lettersStr = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz'
class PasswordGenerate:
    password_of_numbers = ''
    password_of_simblos = ''
    password_of_letters = ''

    def generateCombinationNumbers(self, numbers):
        self.password_of_numbers = numbers
        print(list(permutations(self.password_of_numbers)))
        self.password_of_numbers = ''
    
    def generateCombinationSimbols(self, simbols):
        self.password_of_simblos = simbols
        print(list(permutations(self.password_of_simblos)))
        self.password_of_simblos = ''

    def generateCombinationLetters(self, letters):
        self.password_of_letters = letters
        print(list(permutations(self.password_of_letters)))
        self.password_of_letters = ''

    def generateAllCombination(self, str_password):
        for i in str_password:
            if i in numbersStr:
                self.password_of_numbers += i
            elif i in simbolsStr:
                self.password_of_simblos += i
            else:
                self.password_of_letters += i
        print(list(permutations(self.password_of_numbers)))
        print(list(permutations(self.password_of_simblos)))
        print(list(permutations(self.password_of_letters)))

myClass = PasswordGenerate()
myClass.generateCombinationNumbers(input('Press input numbers: '))
myClass.generateCombinationSimbols(input('Press input special simbols: '))
myClass.generateCombinationLetters(input('Press input letters: '))
myClass.generateAllCombination(input('Press input string of password: '))