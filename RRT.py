from tkinter import *
from tkinter import ttk
import random

def ErrorClose():
    global errorOcc, error
    errorOcc = False
    error.destroy()

def ButCreateObstacles():
    global CreateObstacles, CreateRobot, CreateTarget, ClearGrid, StartSim, SizeChange, robot, target, clicked, ListChoose, ClearRes
    CreateObstacles['text'] = 'Расставить препятствия'
    CreateObstacles['command'] = PlaceObstacles
    SizeChange['state'] = NORMAL
    CreateRobot['state'] = NORMAL
    CreateTarget['state'] = NORMAL
    ClearGrid['state'] = NORMAL
    ListChoose['state'] = NORMAL
    ClearRes['state'] = NORMAL
    if robot and target:
        StartSim['state'] = NORMAL
    
def ButCreateRobot():
    global CreateObstacles, CreateRobot, CreateTarget, ClearGrid, StartSim, SizeChange, robot, target, clicked, ListChoose, ClearRes
    CreateRobot['text'] = 'Поместить робота'
    CreateRobot['command'] = PlaceRobot
    SizeChange['state'] = NORMAL
    CreateObstacles['state'] = NORMAL
    CreateTarget['state'] = NORMAL
    ClearGrid['state'] = NORMAL
    ListChoose['state'] = NORMAL
    ClearRes['state'] = NORMAL
    if robot and target:
        StartSim['state'] = NORMAL
    
def ButCreateTarget():
    global CreateObstacles, CreateRobot, CreateTarget, ClearGrid, StartSim, SizeChange, robot, target, clicked, ListChoose, ClearRes
    CreateTarget['text'] = 'Установить цель'
    CreateTarget['command'] = PlaceTarget
    SizeChange['state'] = NORMAL
    CreateRobot['state'] = NORMAL
    CreateObstacles['state'] = NORMAL
    ClearGrid['state'] = NORMAL
    ListChoose['state'] = NORMAL
    ClearRes['state'] = NORMAL
    if robot and target:
        StartSim['state'] = NORMAL     

def ButStartSim():
    global CreateObstacles, CreateRobot, CreateTarget, ClearGrid, StartSim, SizeChange, robot, target, clicked, ListChoose, ClearRes
    CreateRobot['state'] = DISABLED
    SizeChange['state'] = DISABLED
    CreateObstacles['state'] = DISABLED
    CreateTarget['state'] = DISABLED
    ClearGrid['state'] = DISABLED
    ListChoose['state'] = DISABLED
    ClearRes['state'] = DISABLED
    StartSim['text'] = 'Прервать'
    StartSim['command'] = ButStopSim()
    if ListChoose.get() == 'RRT':
        RRT()
    else:
        RRT_Star()
    
def ButStopSim():
    global CreateObstacles, CreateRobot, CreateTarget, ClearGrid, StartSim, SizeChange, robot, target, clicked, ListChoose, ClearRes
    CreateRobot['state'] = NORMAL
    SizeChange['state'] = NORMAL
    CreateObstacles['state'] = NORMAL
    CreateTarget['state'] = NORMAL
    ClearGrid['state'] = NORMAL
    ListChoose['state'] = NORMAL
    ClearRes['state'] = NORMAL
    StartSim['text'] = 'Начать расчет'
    StartSim['command'] = ButStartSim
    
def ClearResults():
    global c, clicked, robot, target, high, length
    for i in range(high * length):
        if i not in clicked and i != robot and i != target:
            c.itemconfig(i, fill = "white")

def ObstaclesClick(event):
    global c, clicked, robot, target, error, errorLabel, errorOcc, matrix
    ids = c.find_withtag(CURRENT)[0]
    if ids != robot and ids != target:
        if ids not in clicked:
            c.itemconfig(CURRENT, fill = "gray")
            clicked.add(ids)
        else:
            c.itemconfig(CURRENT, fill = "white")
            clicked.remove(ids)
    else:
        if not errorOcc:
            errorOcc = True
            error = Tk()
            error.title('Ошибка!')
            errorLabel = Label(error, height = 1, width = 50)
            errorLabel.pack(padx = 5, pady = 5)
            error.protocol("WM_DELETE_WINDOW", ErrorClose)
        errorLabel['text'] = 'Выбрано некорректное расположение препятствия!'
    c.update()

def PlaceObstacles():
    global c, clicked, CreateObstacles, CreateRobot, CreateTarget, ClearGrid, StartSim, SizeChange, ListChoose, ClearRes
    c.bind("<Button-1>", ObstaclesClick)
    CreateObstacles['text'] = 'Подтвердить \n расположение \n препятствий'
    CreateObstacles['command'] = lambda:[c.unbind("<Button-1>"), ButCreateObstacles()]
    SizeChange['state'] = DISABLED
    CreateRobot['state'] = DISABLED
    CreateTarget['state'] = DISABLED
    ClearGrid['state'] = DISABLED
    ListChoose['state'] = DISABLED
    StartSim['state'] = DISABLED
    ClearRes['state'] = DISABLED

def RobotClick(event):
    global c, robot, clicked, target, error, errorLabel, errorOcc
    ids = c.find_withtag(CURRENT)[0]
    if ids not in clicked and ids != target:
        if robot:
            c.itemconfig(robot, fill = "white")
            robot = 0
        c.itemconfig(CURRENT, fill = "blue")
        robot = ids
    else:
        if not errorOcc:
            errorOcc = True
            error = Tk()
            error.title('Ошибка!')
            errorLabel = Label(error, height = 1, width = 50)
            errorLabel.pack(padx = 5, pady = 5)
            error.protocol("WM_DELETE_WINDOW", ErrorClose)
        errorLabel['text'] = 'Выбрано некорректное расположение робота!'
    c.update()

def PlaceRobot():
    global c, robot, CreateObstacles, CreateRobot, CreateTarget, ClearGrid, StartSim, SizeChange, ListChoose, ClearRes
    c.bind("<Button-1>", RobotClick)
    if robot:
        c.itemconfig(robot, fill = "white")
        robot = 0
    CreateRobot['text'] = 'Подтвердить \n расположение \n робота'
    CreateRobot['command'] = lambda:[c.unbind("<Button-1>"), ButCreateRobot()]
    SizeChange['state'] = DISABLED
    CreateObstacles['state'] = DISABLED
    CreateTarget['state'] = DISABLED
    ClearGrid['state'] = DISABLED
    ListChoose['state'] = DISABLED
    StartSim['state'] = DISABLED
    ClearRes['state'] = DISABLED

def TargetClick(event):
    global c, target, clicked, robot, error, errorLabel, errorOcc
    ids = c.find_withtag(CURRENT)[0]
    if ids not in clicked and ids != robot:
        if target:
            c.itemconfig(target, fill = "white")
            target = 0
        c.itemconfig(CURRENT, fill = "red")
        target = ids
    else:
        if not errorOcc:
            errorOcc = True
            error = Tk()
            error.title('Ошибка!')
            errorLabel = Label(error, height = 1, width = 50)
            errorLabel.pack(padx = 5, pady = 5)
            error.protocol("WM_DELETE_WINDOW", ErrorClose)
        errorLabel['text'] = 'Выбрано некорректное расположение цели!'
    c.update()

def PlaceTarget():
    global c, target, CreateObstacles, CreateRobot, CreateTarget, ClearGrid, StartSim, SizeChange, ListChoose, ClearRes
    c.bind("<Button-1>", TargetClick)
    if target:
        c.itemconfig(target, fill = "white")
        target = 0
    CreateTarget['text'] = 'Подтвердить \n расположение \n цели'
    CreateTarget['command'] = lambda:[c.unbind("<Button-1>"), ButCreateTarget()]
    SizeChange['state'] = DISABLED
    CreateRobot['state'] = DISABLED
    CreateObstacles['state'] = DISABLED
    ClearGrid['state'] = DISABLED
    ListChoose['state'] = DISABLED
    StartSim['state'] = DISABLED
    ClearRes['state'] = DISABLED

def EnvironmentClear():
    global c, StartSim, robot, target, clicked, high, length
    for i in range(high * length):
        c.itemconfig(i, fill = "white")
    clicked.clear()
    robot = 0
    target = 0
    StartSim['state'] = DISABLED

def RRT():
    global c, clicked, robot, target
    global high, length
    Distances = dict()
    Parents = dict()
    Parents[robot] = ''
    Distances[robot] = 0
    Nodes = set()
    Nodes.add(robot)
    AvailableNum = [i for i in range(high * length)]
    for i in clicked:
        AvailableNum.remove(i)
    AvailableNum.remove(robot)
    for i in AvailableNum:
        if i + 1 != target:
            c.itemconfig(i + 1, fill = "white")
    OK = False
    while not OK:
        ind = random.choice(AvailableNum)
        i = (ind - 1) % high
        j = (ind - 1) // high
        MinDist = high + length
        for num in Nodes:
            m = (num - 1) % high
            n = (num - 1) // high
            if abs(i - m) + abs(j - n) < MinDist:
                MinDist = abs(i - m) + abs(j - n)
                m_nearest = m
                n_nearest = n
        if abs(i - m_nearest) < abs(j - n_nearest):
            if j - n_nearest > 0:
                if ((n_nearest + 1) * high + m_nearest + 1) in AvailableNum:
                    k = (n_nearest + 1) * high + m_nearest + 1
                    Nodes.add(k)
                    AvailableNum.remove(k)
                    c.itemconfig(k, fill="yellow")
                    Distances[k] = Distances[k - high] + 1
                    Parents[k] = k - high
                    if k == target:
                        OK = True
                        c.itemconfig(k, fill = "red")
                        AvailableNum.append(k)
                        while k != robot:
                            k = Parents[k]
                            c.itemconfig(k, fill = "green")
                        c.itemconfig(robot, fill = "blue")
            else:
                if ((n_nearest - 1) * high + m_nearest + 1) in AvailableNum:
                    k = (n_nearest - 1) * high + m_nearest + 1
                    Nodes.add(k)
                    AvailableNum.remove(k)
                    c.itemconfig(k, fill="yellow")
                    Distances[k] = Distances[k + high] + 1
                    Parents[k] = k + high
                    if k == target:
                        OK = True
                        c.itemconfig(k, fill="red")
                        AvailableNum.append(k)
                        while k != robot:
                            k = Parents[k]
                            c.itemconfig(k, fill = "green")
                        c.itemconfig(robot, fill = "blue")
        else:
            if i - m_nearest > 0:
                if (n_nearest * high + m_nearest + 2) in AvailableNum:
                    k = n_nearest * high + m_nearest + 2
                    Nodes.add(k)
                    AvailableNum.remove(k)
                    c.itemconfig(k, fill="yellow")
                    Distances[k] = Distances[k - 1] + 1
                    Parents[k] = k - 1
                    if k == target:
                        OK = True
                        c.itemconfig(k, fill = "red")
                        AvailableNum.append(k)
                        while k != robot:
                            k = Parents[k]
                            c.itemconfig(k, fill = "green")
                        c.itemconfig(robot, fill = "blue")
            else:
                if (n_nearest * high + m_nearest) in AvailableNum:
                    k = n_nearest * high + m_nearest
                    Nodes.add(k)
                    AvailableNum.remove(k)
                    c.itemconfig(k, fill="yellow")
                    Distances[k] = Distances[k + 1] + 1
                    Parents[k] = k + 1
                    if k == target:
                        OK = True
                        c.itemconfig(k, fill = "red")
                        AvailableNum.append(k)
                        while k != robot:
                            k = Parents[k]
                            c.itemconfig(k, fill = "green")
                        c.itemconfig(robot, fill = "blue")  

def RRT_Star():
    global c, clicked, robot, target
    global high, length
    Distances = dict()
    Parents = dict()
    Parents[robot] = ''
    Distances[robot] = 0
    Nodes = set()
    Nodes.add(robot)
    AvailableNum = [i for i in range(high * length)]
    for i in clicked:
        AvailableNum.remove(i)
    AvailableNum.remove(robot)
    for i in AvailableNum:
        if i + 1 != target:
            c.itemconfig(i + 1, fill = "white")
    OK = False
    while not OK:
        ind = random.choice(AvailableNum)
        i = (ind - 1) % high
        j = (ind - 1) // high
        MinDist = high + length
        #print(i, j)
        for num in Nodes:
            m = (num - 1) % high
            n = (num - 1) // high
            if abs(i - m) + abs(j - n) + Distances[n * high + m + 1] <= MinDist and ((n * high + m + 2 in AvailableNum 
                                                                                     and abs(i - m) >= abs(j - n)
                                                                                     and i - m > 0)
                                                                                     or (n * high + m in AvailableNum
                                                                                         and abs(i - m) >= abs(j - n)
                                                                                         and i - m < 0)
                                                                                     or ((n + 1) * high + m + 1 in AvailableNum
                                                                                         and abs(i - m) < abs(j - n)
                                                                                         and j - n > 0)
                                                                                     or ((n - 1) * high + m + 1 in AvailableNum
                                                                                         and abs(i - m) < abs(j - n)
                                                                                         and j - n < 0)):
                MinDist = abs(i - m) + abs(j - n) + Distances[n * high + m + 1]
                m_nearest = m
                n_nearest = n
        #print(m_nearest, n_nearest)
        #print()
        if abs(i - m_nearest) < abs(j - n_nearest):
            if j - n_nearest > 0:
                if ((n_nearest + 1) * high + m_nearest + 1) in AvailableNum:
                    k = (n_nearest + 1) * high + m_nearest + 1
                    Nodes.add(k)
                    AvailableNum.remove(k)
                    c.itemconfig(k, fill="yellow")
                    Distances[k] = Distances[k - high] + 1
                    Parents[k] = k - high
                    if (k + 1) in Nodes and Distances[k] + 1 < Distances[k + 1]:
                        Parents[k + 1] = k
                        Distances[k + 1] = Distances[k] + 1
                    if (k - 1) in Nodes and Distances[k] + 1 < Distances[k - 1]:
                        Parents[k - 1] = k
                        Distances[k - 1] = Distances[k] + 1
                    if (k + high) in Nodes and Distances[k] + 1 < Distances[k + high]:
                        Parents[k + high] = k
                        Distances[k + high] = Distances[k] + 1
                    if k == target:
                        OK = True
                        c.itemconfig(k, fill = "red")
                        AvailableNum.append(k)
                        while k != robot:
                            k = Parents[k]
                            c.itemconfig(k, fill = "green")
                        c.itemconfig(robot, fill = "blue")
            else:
                if ((n_nearest - 1) * high + m_nearest + 1) in AvailableNum:
                    k = (n_nearest - 1) * high + m_nearest + 1
                    Nodes.add(k)
                    AvailableNum.remove(k)
                    c.itemconfig(k, fill="yellow")
                    Distances[k] = Distances[k + high] + 1
                    Parents[k] = k + high
                    if (k + 1) in Nodes and Distances[k] + 1 < Distances[k + 1]:
                        Parents[k + 1] = k
                        Distances[k + 1] = Distances[k] + 1
                    if (k - 1) in Nodes and Distances[k] + 1 < Distances[k - 1]:
                        Parents[k - 1] = k
                        Distances[k - 1] = Distances[k] + 1
                    if (k - high) in Nodes and Distances[k] + 1 < Distances[k - high]:
                        Parents[k - high] = k
                        Distances[k - high] = Distances[k] + 1
                    if k == target:
                        OK = True
                        c.itemconfig(k, fill="red")
                        AvailableNum.append(k)
                        while k != robot:
                            k = Parents[k]
                            c.itemconfig(k, fill = "green")
                        c.itemconfig(robot, fill = "blue")
        else:
            if i - m_nearest > 0:
                if (n_nearest * high + m_nearest + 2) in AvailableNum:
                    k = n_nearest * high + m_nearest + 2
                    Nodes.add(k)
                    AvailableNum.remove(k)
                    c.itemconfig(k, fill="yellow")
                    Distances[k] = Distances[k - 1] + 1
                    Parents[k] = k - 1
                    if (k + 1) in Nodes and Distances[k] + 1 < Distances[k + 1]:
                        Parents[k + 1] = k
                        Distances[k + 1] = Distances[k] + 1
                    if (k - high) in Nodes and Distances[k] + 1 < Distances[k - high]:
                        Parents[k - high] = k
                        Distances[k - high] = Distances[k] + 1
                    if (k + high) in Nodes and Distances[k] + 1 < Distances[k + high]:
                        Parents[k + high] = k
                        Distances[k + high] = Distances[k] + 1
                    if k == target:
                        OK = True
                        c.itemconfig(k, fill = "red")
                        AvailableNum.append(k)
                        while k != robot:
                            k = Parents[k]
                            c.itemconfig(k, fill = "green")
                        c.itemconfig(robot, fill = "blue")
            else:
                if (n_nearest * high + m_nearest) in AvailableNum:
                    k = n_nearest * high + m_nearest
                    Nodes.add(k)
                    AvailableNum.remove(k)
                    c.itemconfig(k, fill="yellow")
                    Distances[k] = Distances[k + 1] + 1
                    Parents[k] = k + 1
                    if (k - 1) in Nodes and Distances[k] + 1 < Distances[k - 1]:
                        Parents[k - 1] = k
                        Distances[k - 1] = Distances[k] + 1
                    if (k - high) in Nodes and Distances[k] + 1 < Distances[k - high]:
                        Parents[k - high] = k
                        Distances[k - high] = Distances[k] + 1
                    if (k + high) in Nodes and Distances[k] + 1 < Distances[k + high]:
                        Parents[k + high] = k
                        Distances[k + high] = Distances[k] + 1
                    if k == target:
                        OK = True
                        c.itemconfig(k, fill = "red")
                        AvailableNum.append(k)
                        while k != robot:
                            k = Parents[k]
                            c.itemconfig(k, fill = "green")
                        c.itemconfig(robot, fill = "blue")

def OccupancyGrid():
    global c, CreateObstacles, CreateRobot, CreateTarget, ClearGrid, ListChoose, StartSim, ClearRes, SizeChange, high, length
    root = Tk()
    root.title('Карта местности')
    OptionsFrame = Frame(root)
    OptionsFrame.pack(expand = True, side = LEFT)
    SizeChange = Button(OptionsFrame, text = 'Размер поля', command = lambda:[root.destroy(), SizeSettings()], width = 20)
    SizeChange.pack(padx = 5, pady = 5)
    CreateObstacles = Button(OptionsFrame, text = 'Расставить препятствия', command = PlaceObstacles, width = 20)
    CreateObstacles.pack(padx = 5, pady = 5)
    CreateRobot = Button(OptionsFrame, text = 'Поместить робота', command = PlaceRobot, width = 20)
    CreateRobot.pack(padx = 5, pady = 5)
    CreateTarget = Button(OptionsFrame, text = 'Установить цель', command = PlaceTarget, width = 20)
    CreateTarget.pack(padx = 5, pady = 5)
    ClearGrid = Button(OptionsFrame, text = 'Очистить поле', command = EnvironmentClear, width = 20)
    ClearGrid.pack(padx = 5, pady = 5)
    LabelChoose = Label(OptionsFrame, height = 2, text = 'Выберите метод \nмоделирования:')
    LabelChoose.pack(padx = 5, pady = 5)
    ListChoose = ttk.Combobox(OptionsFrame, values = ['RRT', 'RRT*'])
    ListChoose.pack(padx = 5)
    ListChoose.current(0)
    StartSim = Button(OptionsFrame, text = 'Начать расчет', state = DISABLED, command = ButStartSim, width = 20)
    StartSim.pack(padx = 5, pady = 5)
    ClearRes = Button(OptionsFrame, text = 'Очистить результаты \nмоделирования', command = ClearResults, width = 20)
    ClearRes.pack(padx = 5, pady = 5)
    StopProgramm = Button(OptionsFrame, text = 'Выход', command = lambda:[root.destroy()], width = 20)
    StopProgramm.pack(padx = 5, pady = 5)
    size = 10
    c = Canvas(root, width = length * size, height = high * size)
    c.pack(side = LEFT)
    for i in range(length):
        for j in range(high):
            c.create_rectangle(i * size, j * size, (i + 1) * size, (j + 1) * size, fill = "white")
     
def CheckCor():
    global error, errorLabel, errorOcc, high, length
    if lengthText.get('1.0', END) == '\n' and highText.get('1.0', END) == '\n':
        length = 50
        high = 50
        settings.destroy()
        OccupancyGrid()
    elif lengthText.get('1.0', END) != '\n' and highText.get('1.0', END) == '\n':
        try:
            length = int(lengthText.get('1.0', END))
            if length >= 2:
                high = 10
                settings.destroy()
                OccupancyGrid()
            else:
                if not errorOcc:
                    errorOcc = True
                    error = Tk()
                    error.title('Ошибка!')
                    errorLabel = Label(error, height = 1, width = 30)
                    errorLabel.pack(padx = 5, pady = 5)
                    error.protocol("WM_DELETE_WINDOW", ErrorClose)
                errorLabel['text'] = 'Введите целые числа, большие 1!'
        except Exception:
            if not errorOcc:
                errorOcc = True
                error = Tk()
                error.title('Ошибка!')
                errorLabel = Label(error, height = 1, width = 30)
                errorLabel.pack(padx = 5, pady = 5)
                error.protocol("WM_DELETE_WINDOW", ErrorClose)
            errorLabel['text'] = 'Введите целые числа, большие 1!'
    elif lengthText.get('1.0', END) == '\n' and highText.get('1.0', END) != '\n':
        try:
            high = int(highText.get('1.0', END))
            if high >= 2:
                length = 10
                settings.destroy()
                OccupancyGrid()
            else:
                if not errorOcc:
                    errorOcc = True
                    error = Tk()
                    error.title('Ошибка!')
                    errorLabel = Label(error, height = 1, width = 30)
                    errorLabel.pack(padx = 5, pady = 5)
                    error.protocol("WM_DELETE_WINDOW", ErrorClose)
                errorLabel['text'] = 'Введите целые числа, большие 1!'
        except Exception:
            if not errorOcc:
                errorOcc = True
                error = Tk()
                error.title('Ошибка!')
                errorLabel = Label(error, height = 1, width = 30)
                errorLabel.pack(padx = 5, pady = 5)
                error.protocol("WM_DELETE_WINDOW", ErrorClose)
            errorLabel['text'] = 'Введите целые числа, большие 1!'
    else:
        try:
            length = int(lengthText.get('1.0', END))
            high = int(highText.get('1.0', END))
            if high >= 2 and length >=2:
                settings.destroy()
                OccupancyGrid()
            else:
                if not errorOcc:
                    errorOcc = True
                    error = Tk()
                    error.title('Ошибка!')
                    errorLabel = Label(error, height = 1, width = 30)
                    errorLabel.pack(padx = 5, pady = 5)
                    error.protocol("WM_DELETE_WINDOW", ErrorClose)
                errorLabel['text'] = 'Введите целые числа, большие 1!'
        except Exception:
            if not errorOcc:
                errorOcc = True
                error = Tk()
                error.title('Ошибка!')
                errorLabel = Label(error, height = 1, width = 30)
                errorLabel.pack(padx = 5, pady = 5)
                error.protocol("WM_DELETE_WINDOW", ErrorClose)
            errorLabel['text'] = 'Введите целые числа, большие 1!'
    
def SizeSettings():
    global settings, lengthText, highText, robot, target, clicked, errorOcc
    robot = 0
    target = 0
    clicked = set()
    errorOcc = False
    settings = Tk()
    settings.title('Настройки')
    settings.geometry('200x100')
    lengthText = Text(settings, width = 5, height = 1)
    lengthLabel = Label(settings, height = 1, text = 'Длина')
    highText = Text(settings, width = 5, height = 1)
    highLabel = Label(settings, height = 1, text = 'Ширина')
    lengthText.place(x = 75, y = 5)
    lengthLabel.place(x = 5, y = 5)
    highText.place(x = 75, y = 35)
    highLabel.place(x = 5, y = 35)
    lengthText.insert(END, 50)
    highText.insert(END, 50)
    Btn = Button(settings, text = 'Начать', command = CheckCor)
    Btn.place(x = 75, y = 65)
    settings.mainloop()
    
SizeSettings()
