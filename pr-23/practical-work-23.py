from threading import Thread
from os.path import dirname
from random import randint, choice
from time import sleep

class Greeting:
    def __init__(self, name):
        self.name = name
    def trueGreeting(self, newName):
        with open(dirname(__file__) + "/wordsGreeting.txt", "r") as wordsGreeting:
            print(choice(wordsGreeting.readlines()),
            "Можешь величать меня как БОТ ЕБС\n",
            'Кстати тут написанно что все кого зовут "{}" туповатые'.format(newName))
    def comicGreeting(self):
        with open(dirname(__file__) + "/alphabet.txt", "r") as alphabet:
            counter = 0
            for line in alphabet:
                if len(self.name) != 0 and self.name[0].lower() in line:
                    break
                counter += 1
            if counter == 0:
                print("Вот это по нашему!\nРУССКИЕ ВПЕРЁД\nРУССКИЕ ВПЕРЁД\nРУССКИЕ ВПЕРЁД\nНо будь добр напиши своё красивое славянское имя ещё раз")
            elif counter == 1:        
                print("Ха! подумал я на пендоском базарить буду, неее пиши на русском")
            elif counter == 2:
                print("Я тебе щас твой 10-ричный код знаешь куда засуну! Это оскорбление чувств бота!\nНа русском пиши шпрых")
            elif counter == 3:
                print("Ты шо дурак?")

class SaverUserAnsver(Thread):
    def __init__(self, a, box):
        Thread.__init__(self)
        self.answer = a
        self.Containerer = box
    def run(self):
        self.Containerer.write(self.answer + "\n")

class BotDialog(Thread):
    def __init__(self, ui):
        Thread.__init__(self)
        self.userInput = ui
    def createContainer(self):
        self.wordsContainer = []
        with open(dirname(__file__) + "/botWords.txt", "r") as botWords:
            self.wordsContainer.extend(botWords.readlines())
        with open(dirname(__file__) + "/answerUser.txt", "r") as ContainerUserInput:
            self.wordsContainer.extend(ContainerUserInput.readlines())
    def run(self):
        self.createContainer()
        self.botAnswer = choice(self.wordsContainer)
        print("Бот ЕБС: " + self.botAnswer)

class CorrectorBot(Thread):
    def __init__(self, ba):
        Thread.__init__(self)
        self.botAnswer = ba
    def run(self):
        if input("Вам понравился этот ответ? д/н\n").lower() == "н":
            with open(dirname(__file__) + "/botWords.txt", "r") as botWords:
                botWordsStr = botWords.read()
                with open(dirname(__file__) + "/answerUser.txt", "r") as answerUser:
                    answerUserStr = answerUser.read()
                    if self.botAnswer in botWordsStr:
                        #проверяет из какого файла был выдан ответ
                        with open(dirname(__file__) + "/botWords.txt", "w") as botWords2:
                            botWords2.write(botWordsStr.replace(self.botAnswer, ""))
                            #записывает в файл всё что прочёл без самого ответа
                    elif self.botAnswer in answerUserStr:
                        with open(dirname(__file__) + "/answerUser.txt", "w") as answerUser2:
                            answerUser2.write(answerUserStr.replace(self.botAnswer, ""))
            with open(dirname(__file__) + "/muteWords.txt", "a") as muteWords:
                muteWords.write(self.botAnswer)

def main():
    ContainerUserInput = open(dirname(__file__) + "/answerUser.txt", "a")
    #ответы пользователя занесутся после окончания программы, закрывется на 96 строке
    name = input("Hi User! What you name?\n")
    greeting = Greeting(name)
    saverUserAnsver = SaverUserAnsver(name, ContainerUserInput)
    saverUserAnsver.start()
    greeting.comicGreeting()
    newName = input()
    greeting.trueGreeting(newName)
    saverUserAnsver = SaverUserAnsver(newName, ContainerUserInput)
    saverUserAnsver.start()
    while True:
        userAnswer = input(newName + ": ")
        if userAnswer.lower() == "пока":
            break
        botDialog = BotDialog(userAnswer)
        saverUserAnsver = SaverUserAnsver(userAnswer, ContainerUserInput)
        botDialog.start()
        botDialog.join()
        correctorBot = CorrectorBot(botDialog.botAnswer)
        saverUserAnsver.start()
        correctorBot.start()
    sleep(1)
    #ждём пока сохраняться изменения пользователя
    ContainerUserInput.close()

if __name__ == '__main__':
    main()