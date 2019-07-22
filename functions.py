tasks = []


def printTasks():
    for i in range(len(tasks)):
        print(str(i), end=" - ")
        print(tasks[i])


def updateTask():
    print('Enter the index of the task: ', end='')
    Tindex = int(input())
    if Tindex > len(tasks) - 1:
        print("ERROR!!Please enter a valid index!!!")
        return
    print('Enter the description of the task: ', end='')
    Tdes = input()
    tasks[Tindex]['description'] = Tdes 
    printTasks()      


def newTask():
    print('Enter the name of the task: ', end='')
    Tname = input()
    print('Enter the description of the task: ', end='')
    Tdes = input()
    tasks.append({'name':Tname,'description':Tdes})
    printTasks()


def deleteTask():
    print('Enter the index of the task: ', end='')
    Tindex = int(input())
    if Tindex <= len(tasks) - 1:
        del tasks[Tindex]
        return 
    print("ERROR!!Please enter a valid index!!!")
    printTasks()

