import os
try:
    os.mkdir(os.path.dirname(__file__) + '/myDef')
except FileExistsError:
    pass
def counter(value):
    with open(os.path.dirname(__file__) + '/myDef/check.txt', 'w') as function:
        if value == 1:
            myFile.seek(10)
            function.write('Пароль:\n' + myFile.read())
        else:
            function.write('Пароль не найден')
def total():
    with open(os.path.dirname(__file__) + '/myDef/check.txt', 'r') as function:
        for line in function:
            print(line)
for i in list(os.walk(os.path.dirname(__file__)))[0][2]:
    if len(list(os.walk(os.path.dirname(__file__)))[0][2]) == 1:
        print('В папке нет txt файлов')
        counter(0)
        break
    with open(os.path.dirname(__file__) + '/' +i, 'r') as myFile:
        if myFile.read(8) == 'password':
            counter(1)
            break
        else:
            counter(0)
total()