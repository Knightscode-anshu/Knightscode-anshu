tasklist=[]
def start():
    print("Instructions:")
    print("Enter '1' to add a task")
    print("Enter '2' to remove a task")
    print("Enter '3' to view a task")
    print("Enter '4' to exit")    
    while True:       
        t=int(input())
        if t==1:
            a=input()
            tasklist.append(a)
            print("task added")    
        elif t==2:
            b=int(input("Enter the index of the task to be removed:"))
            if len(tasklist)==0:
                print("There are no tasks in the list")    
            elif 0<=b<len(tasklist):
                tasklist.pop(b)
                print("task removed")                
            else:
                print("Invalid input")                
        elif t==3:
            c=int(input("Enter the index of the task to view:"))   
            if 0<=c<len(tasklist):
                print("The task is:",tasklist[c])                
            else:
                print("Invalid input")                
        elif t==4:
            print("Stopping the application")
            break                    
start()



