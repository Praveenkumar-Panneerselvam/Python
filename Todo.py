Tasks=[]
def show_menu():
    print("1.Add Tasks")
    print("2.View Tasks")
    print("3.Remove Tasks")
    print("4.Mark Tasks as completed")
    print("5.Exit")

def Add_tasks():
    task=input("Enter the task: ")
    if task:
        Tasks.append({"text":task,"completed":False})
        print("Task added")
    else:
        print("Task is empty,Add Task")

def View_Tasks():
    if not Tasks:
        print("No Task")
    else:
        print("\n Your Tasks")
        for i,t in enumerate(Tasks,start=1):
            if t["completed"] ==True:
                status="*"
            else:
                status=""
            print(f"{i}.[{status}]{t['text']}")
    
def Remove_Tasks():
    if not Tasks:
        print("NoTask in the list")
        View_Tasks()
    else:
        try:
            index=int(input("Enter the task number to remove"))
            if 1<=index<=len(Tasks):
                removed=Tasks.pop(index-1)
                print(f"{removed['text']} is succesfully removed")
            else:
                print("Invalid Number")
        except ValueError:
            print("Enter a valid number")

def Mark_Tasks():
    if not Tasks:
        print("No Tasks")
        View_Tasks()
    else:
        try:
            index=int(input("Please Enter a index Number to Mark completed"))
            if 1<= index <=len(Tasks):
                Tasks[index-1]["completed"]=True
                print("Task Mark completed")
            else:
                print("Invalid Number")
        except ValueError:
            print("Enter the valid number")

def main():
    while True:
        show_menu()
        choice=int(input("Choose the number from(1-5)"))
        if choice==1:
            Add_tasks()
        elif choice==2:
            View_Tasks()
        elif choice==3:
            Remove_Tasks()
        elif choice==4:
            Mark_Tasks()
        elif choice==5:
            print("Good bye!")
        else:
            print("Invalid choice")
if __name__=="__main__":
    main()

