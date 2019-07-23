import functions


def run():

    inputVal=0
    print("=====Welcome to Todo App=====")

    while(True):
        print("""
1- Press 1 to create a new task.
2- Press 2 to list all the tasks.
3- Press 3 to update a task.
4- Press 4 to delete a task.
5- Press 5 to insert at a specific index.
5- Press 6 to Exit.""")

        print("\nEnter your input: ")
        inputVal = int(input())

        if inputVal == 1:
            functions.New_task()
        elif inputVal == 2:
            functions.Print_tasks()
        elif inputVal == 3:
            functions.Update_task()           
        elif inputVal == 4:
            functions.Delete_task()
        elif inputVal == 5:
            functions.Insert_task()
        else:
            break
    

if __name__ == "__main__":
    run()
