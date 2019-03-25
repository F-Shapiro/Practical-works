import tkinter as GUI
from tkinter import ttk
from random import randint
def getResExam():
    readableRes = "2.3.4.5"
    if inputUser.get() in readableRes:
        verdictTopTeacher.configure(text = "Вы сдали программирование на {}".format(inputUser.get()))
        verdictTopTeacher.configure(backgroun = "#B76E79")
    else:
        verdictTopTeacher.configure(text = "Спулае мулае, алкоподобный синтаксис")
        verdictTopTeacher.configure(backgroun = "#B76E79")
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
        frame.configure(height = 3, width = 3)
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
window.configure(background = "white")

style = ttk.Style().configure("TLabel", relief = "flat", background = "#B76E79")
style = ttk.Style().configure("TButton", relief = "flat", background = "#B76E79")

deathRattle = ttk.Label(window, text = "Я сдам программирование на", font = ("Georgia", 13))
verdictTopTeacher = ttk.Label(window, text = "", font = ("Georgia", 15))
verdictTopTeacher.configure(relief = "flat", background = "white")
inputUser = ttk.Entry(window, width = 5)
frame = ttk.Frame(window, height = 40, width = 70)
retakeExam = ttk.Button(frame, text = "Сдать!", command = getResExam)#, background = "brown", foreground = "white", font = "20", command = getResExam)

window.bind("<KeyPress>", resultExam)
frame.pack_propagate(0)

deathRattle.place(x=0)
inputUser.place(x=250, y=4)
frame.place(x=205, y=115)
retakeExam.pack(fill = GUI.BOTH, expand = 1)
verdictTopTeacher.place(x=80, y=230)
window.mainloop()