import os

tasks = []

def printTasks():
    for i in range(len(tasks)):
        print(str(i), end=" - ")
        print(tasks[i])

def updateTask(Tindex,Tdes):
    if Tindex <= len(tasks)-1:
        tasks[Tindex]['description']=Tdes
    else:
        print("ERROR!!Please enter a valid index!!!")

def newTask(Tname,Tdes):
    newTask={}
    newTask['name']=Tname
    newTask['description']=Tdes
    tasks.append(newTask)


def run():

    title = "=====Welcome to Todo App====="
    inputVal = 0
    print(title)

    while(True):
        print("""
1- Press 1 to create a new task.
2- Press 2 to list all the tasks.
3- Press 3 to update a task.
4- Press 4 to delete a task.
5- Press 5 to Exit.""")

        print("\n\nEnter your input: ")
        inputVal = int(input())

        if inputVal == 1:
            print('Enter the name of the task: ', end='')
            Tname = input()
            print('Enter the description of the task: ', end='')
            Tdes = input()
            newTask(Tname,Tdes)
           

        elif inputVal == 2:
            printTasks()

        elif inputVal == 3:
            print('Enter the index of the task: ', end='')
            Tindex = int(input())
            print('Enter the description of the task: ', end='')
            Tdes = input()
            updateTask(Tindex,Tdes)
            

        elif inputVal == 4:
            print('Enter the index of the task: ', end='')
            Tindex = int(input())
            if Tindex<=len(tasks)-1:
                del tasks[Tindex]
            else:
                print("ERROR!!Please enter a valid index!!!")
        else:
            break



if __name__ == "__main__":
    run()
