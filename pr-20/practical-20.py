import tkinter as GUI
from random import randint
def getResExam():
    readableRes = "2.3.4.5"
    if inputUser.get() in readableRes:
        verdictTopTeacher.configure(text = "Вы сдали программирование на {}".format(inputUser.get()))
    else:
        verdictTopTeacher.configure(text = "Спулае мулае, алкоподобный синтаксис")
def relocation(event):
    frame.place(x = randint(30, 470), y = randint(30, 270))
def resultExam(event):
    if inputUser.get() == "2":
        frame.unbind("<Motion>")
        frame.place(x=205, y=115)
        frame.configure(height = 100, width = 130)
    elif inputUser.get() == "3":
        frame.unbind("<Motion>")
        frame.place(x=205, y=115)
        frame.configure(height = 1, width = 1)
    elif inputUser.get() == "4":
        frame.configure(height = 40, width = 70)
        retakeExam.bind("<Motion>", relocation)
    elif inputUser.get() == "5":
        frame.place_forget()
    else:
        retakeExam.unbind("<Motion>")
        frame.place(x=205, y=115)
        frame.configure(height = 40, width = 70)
window = GUI.Tk()
window.title("Тест на лолку")
window.geometry("500x300")
window.configure(background = "gray")

deathRattle = GUI.Label(window, text = "Я сдам программирование на", font = ("Georgia", 13))
verdictTopTeacher = GUI.Label(window, text = "", background = "Gray", font = ("Georgia", 15))
inputUser = GUI.Entry(window, width = 5)
frame = GUI.Frame(window, height = 40, width = 70)
retakeExam = GUI.Button(frame, text = "Сдать!", background = "brown", foreground = "white", font = "20", command = getResExam)

window.bind("<KeyPress>", resultExam)
frame.pack_propagate(0)

deathRattle.place(x=0)
inputUser.place(x=250, y=4)
frame.place(x=205, y=115)
retakeExam.pack(fill = GUI.BOTH, expand = 1)
verdictTopTeacher.place(x=80, y=230)
window.mainloop()