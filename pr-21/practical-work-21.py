import tkinter as GUI
from time import time
from random import choice
from os.path import dirname
coordinate = []
'''
массив всех возможных координатов в допустимой области, что бы не за спавнится на пакмене или за краями
'''
for xy in range(100, 320):
    coordinate.append(xy)
for xy2 in range(480, 700):
    coordinate.append(xy2)
with open(dirname(__file__) + "/caseTarget.txt", "w") as statusTarget:
    statusTarget.write("")
#фунция ranCoor(num) возвращает рандомные допустимые координаты для целей
def ranCoor(num):
    '''
    аргумент num служит для определения оси координат и повторается ли она
    '''
    if num == 0:
        with open(dirname(__file__) + "/buffDigitX.txt", "w") as buffDigitX:
            buff = choice(coordinate)
            buffDigitX.write(str(buff))
            coordinate.remove(buff)
        return buff
    elif num == 1:
        with open(dirname(__file__) + "/buffDigitY.txt", "w") as buffDigitY:
            buff = choice(coordinate)
            buffDigitY.write(str(buff))
            coordinate.remove(buff)
        return buff
    elif num == 2:
        with open(dirname(__file__) + "/buffDigitX.txt", "r") as buffDigitX:
            return int(buffDigitX.read()) + 20
    elif num == 3:
        with open(dirname(__file__) + "/buffDigitY.txt", "r") as buffDigitY:
            return int(buffDigitY.read()) + 20
#фунция controlHeroMoving() отвечает за анимацию и передвижение пакмена
def controlHeroMoving(event):
    #функция angle(start, extend, coor) отвечает за анимацию, она меняет угол пакмена
    def angle(start, extend, coor):
        '''
        ервые два аргумента соответствуют аргументам объекта canvas создаваемого create_arc
        с помощью аргумента coor передаётся индекс элемент списка координат текущего расположения пакмена
        на каждой координате кратной 5 без остатка пакмен будет закрывать рот
        '''
        if gameBody.coords(mainHero)[coor]%5 == 0:
            gameBody.itemconfig(mainHero, start = start - 10, extent = extend + 20)
        else:
            gameBody.itemconfig(mainHero, start = start, extent = extend)
    try:
        if event.char == "w":
            angle(110, 320, 1)
            gameBody.move(mainHero, 0, -7)
        elif event.char == "s":
            angle(290, 320, 1)
            gameBody.move(mainHero, 0, 7)
        elif event.char == "d":
            angle(20, 320, 0)
            gameBody.move(mainHero, 7, 0)
        elif event.char == "a":
            angle(200, 320, 0)
            gameBody.move(mainHero, -7, 0)
    '''
    постоянно вылетает ошибка IndexError но программа сбоев на даёт
    '''
    except IndexError:
        pass

#фунция gameProcess() отвечает за игровой процесс и его итог
def gameProcess(event):
    #функция checkDieTarget() проверяет исчезли ли все цели и если да то выводит итог игры
    def checkDieTarget():
        with open(dirname(__file__) + "/caseTarget.txt", "r") as caseTarget:
            if caseTarget.read() == "00000":
                final = time()
                if int(final - begin) > 10:
                    gameResult.configure(text = "Time up! You lose! {}sec".format(int(final - begin)))
                    gameBody.delete(mainHero)
                elif int(final - begin) < 10:
                    gameResult.configure(text = "You win! {}sec".format(int(final - begin)))
                    gameBody.coords(mainHero, gameBody.coords(mainHero)[0]-40, gameBody.coords(mainHero)[1]-40, gameBody.coords(mainHero)[2]+40, gameBody.coords(mainHero)[3]+40)
    #функция controlTarget() отвечает за поведение целей
    def controlTarget():
        #функция checkPos() проверяет находиться ли в области пакмена цель и если да удаляет её
        def checkPos(contain):
            counter = 0
            try:
                if allTarget[contain][0] in range(int(gameBody.coords(mainHero)[0]), int(gameBody.coords(mainHero)[2])) and allTarget[contain][2] in range(int(gameBody.coords(mainHero)[0]), int(gameBody.coords(mainHero)[2])):#проверка координатов по x
                    counter += 1
                if allTarget[contain][1] in range(int(gameBody.coords(mainHero)[1]), int(gameBody.coords(mainHero)[3])) and allTarget[contain][3] in range(int(gameBody.coords(mainHero)[1]), int(gameBody.coords(mainHero)[3])):#проверка координатов по y
                    counter += 1
            '''
            после исчезновения 1ой цели начинает выплывать эта ошибка и ф-ия не рабоает(цели не "поедаются")
            '''
            except IndexError:
                pass
            if counter == 2:
                gameBody.delete(contain)
                with open(dirname(__file__) + "/caseTarget.txt", "a") as statusTarget:
                    statusTarget.write("0")
                checkDieTarget()
        allTarget = {target1:gameBody.coords(target1), target2:gameBody.coords(target2), target3:gameBody.coords(target3), target4:gameBody.coords(target4), target5:gameBody.coords(target5)}#слоаврь нужен для того что бы указать и координаты и сам объект(цель) иначе удалить объект нельзя
        '''
        map для более удобного перебора всех объектов(целей)                                           
        '''
        list(map(checkPos, allTarget))
    controlTarget()

root = GUI.Tk()
root.title("Pyckman")
root.geometry("800x800")
gameBody = GUI.Canvas(root, width = 800, height = 800)
gameResult = GUI.Label(root, text = "", font = ("Georgia", 15))
mainHero = gameBody.create_arc(360, 360, 440, 440, start = 20, extent = 320, outline = "black", fill = "yellow", width = 2)#пакмен
target1 = gameBody.create_oval(ranCoor(0), ranCoor(1), ranCoor(2), ranCoor(3), outline = "black", fill = "red", width = 1)
target2 = gameBody.create_oval(ranCoor(0), ranCoor(1), ranCoor(2), ranCoor(3), outline = "black", fill = "red", width = 1)
target3 = gameBody.create_oval(ranCoor(0), ranCoor(1), ranCoor(2), ranCoor(3), outline = "black", fill = "red", width = 1)
target4 = gameBody.create_oval(ranCoor(0), ranCoor(1), ranCoor(2), ranCoor(3), outline = "black", fill = "red", width = 1)
target5 = gameBody.create_oval(ranCoor(0), ranCoor(1), ranCoor(2), ranCoor(3), outline = "black", fill = "red", width = 1)#цели
gameBody.focus_set()
gameBody.pack()
gameResult.place(x=360, y=10)
gameBody.bind("<KeyPress>", controlHeroMoving)
root.bind("<KeyPress>", gameProcess)

begin = time()
root.mainloop()