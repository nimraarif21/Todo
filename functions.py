tasks = []


def Print_tasks():
    for i in range(len(tasks)):
        print(str(i), end=" - ")
        print(tasks[i])


def Update_task():
    print('Enter the index of the task: ', end='')
    Tindex = int(input())
    if Tindex > len(tasks) - 1:
        print("ERROR!!Please enter a valid index!!!")
        return
    print('Enter the description of the task: ', end='')
    Tdes = input()
    tasks[Tindex]['description'] = Tdes 
    Print_tasks()      


def New_task():
    print('Enter the name of the task: ', end='')
    Tname = input()
    print('Enter the description of the task: ', end='')
    Tdes = input()
    tasks.append({'name':Tname,'description':Tdes})
    Print_tasks()


def Insert_task():
    print('Enter the name of the task: ', end='')
    Tname = input()
    print('Enter the description of the task: ', end='')
    Tdes = input()
    print('Enter the index where you want to insert: ', end='')
    Tindex = int(input())
    if Tindex==0 and len(tasks)==0:
            tasks.insert(Tindex,{'name':Tname,'description':Tdes})
            Print_tasks()
    elif Tindex <= len(tasks)-1:
            tasks.insert(Tindex,{'name':Tname,'description':Tdes})
            Print_tasks()

    else:
            print("ERROR!!Please enter a valid index!!!")


def Delete_task():
    print('Enter the index of the task: ', end='')
    Tindex = int(input())
    if Tindex <= len(tasks) - 1:
        del tasks[Tindex]
        return 
    print("ERROR!!Please enter a valid index!!!")
    Print_tasks()

