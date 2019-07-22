import functions

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
            functions.newTask()
        elif inputVal == 2:
            functions.printTasks()
        elif inputVal == 3:
            functions.updateTask()           
        elif inputVal == 4:
            functions.deleteTask()
        else:
            break



if __name__ == "__main__":
    run()
