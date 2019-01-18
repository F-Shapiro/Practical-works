from itertools import permutations
class PasswordGenerate:
    numbers_in_password = ''
    simblos_in_password = ''
    letters_in_password = ''

    def generateNumbers(self, numbers):
        self.numbers_in_password = numbers
        print(list(permutations(self.numbers_in_password)))
    
    def generateSimbols(self, simbols):
        self.simblos_in_password = simbols
        print(list(permutations(self.simblos_in_password)))

    def generateLetters(self, letters):
        self.letters_in_password = letters
        print(list(permutations(self.letters_in_password)))

    def all_refresh(self, numbers, simbols, letters):
        self.numbers_in_password = numbers
        self.simblos_in_password = simbols
        self.letters_in_password = letters
        print(
            list(permutations(self.numbers_in_password)),
            list(permutations(self.simblos_in_password)),
            list(permutations(self.letters_in_password))
            )

myClass=PasswordGenerate()
myClass.generateNumbers('789')
myClass.generateSimbols('%^&')
myClass.generateLetters('GIT')
myClass.all_refresh('123', '@#$', 'ABC')