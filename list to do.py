def menu():
    print("*****TODAY TO-DO LIST*****")
    print("1.view the list\n2.Add list\n3.Make list as done\n4.Delete the list\n5.Exit")
def view(List):
    if not List:
        print("Your list is empty")
    else:
        print("your lists:")
        for index, task in enumerate(List,1):
            s="done"if task['done']else"to-do"
            print(f"{index}.{task['task']}-{s}")
def add(List):
    task=input("enter task:")
    List.append({'task':task,"done":False})
    print("list added successfully")

def done(List):
    view(List)
    task=int(input("enter list number to mark as done:"))-1
    if 0<=task<len(List):
        List[task]['done']=True
        print("list marked as done")
    else:
        print("invalid list number")
def delete(List):
    view(List)
    task=int(input("enter list number to delete:"))-1
    if 0<=task<len(List):
        del List[task]
        print("list deleted successfully")
    else:
        print("invalid list number")
def main():
    List=[]
    while True:
        menu()
        c=int(input("enter your choice:"))
        if c==1:
            view(List)
        elif c==2:
            add(List)
        elif c==3:
            done(List)
        elif c==4:
            delete(List)
        elif c==5:
            break
        else:
            print("invalid choice")
            
if __name__=="__main__":
  main()
