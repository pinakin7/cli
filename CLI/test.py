import sys
import argparse
from datetime import date
import os
os.chdir(os.getcwd())
str1 = " "
use = '''Usage :-
        $ ./todo add "todo item"  # Add a new todo
        $ ./todo ls               # Show remaining todos
        $ ./todo del NUMBER       # Delete a todo
        $ ./todo done NUMBER      # Complete a todo
        $ ./todo help             # Show usage
        $ ./todo report           # Statistics
'''
if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage='''
    $ ./todo add "todo item"  # Add a new todo
    $ ./todo ls               # Show remaining todos
    $ ./todo del NUMBER       # Delete a todo
    $ ./todo done NUMBER      # Complete a todo
    $ ./todo help             # Show usage
    $ ./todo report           # Statistics
''')
    parser.add_argument("operation",type=str,help="Adds Job to the database",default=None)
    parser.add_argument("type",type=str,nargs='*',help="Adds Job to the database",default=1)
    args = parser.parse_args()

if args.operation == "add":
    todo = str1.join(args.type)
    todo = todo + "\n"
    with open("todo.txt","a") as f:
        f.writelines(todo)
        f.close
    sys.stdout.write("Added todo: {}".format(todo))
elif args.operation == "del":
    with(open("todo.txt","r")) as f:
        lines = f.readlines()
        x = int(str1.join(args.type))
        if x <= len(lines):
            with open("todo.txt","w") as f1:
                f1.writelines(lines[:x-1])
                f1.writelines(lines[x:])
            sys.stdout.write("Deleted todo #{}".format(x))
        else:
            sys.stdout.write("Error: todo #{} does not exist. Nothing deleted".format(x))
elif args.operation == "done":
    with(open("todo.txt","r")) as f:
        lines = f.readlines()
        x = int(str1.join(args.type))
        if x <= len(lines):
            with open("todo.txt","w") as f1:
                f1.writelines(lines[:x-1])
                f1.writelines(lines[x:])
                f1.close
            with open("done.txt","a") as f2:
                task = "x " + str(date.today())+" " + lines[x-1] 
                f2.writelines(task)
            sys.stdout.write("Marked todo #{} as done".format(x))
        else:
            sys.stdout.write("Error: todo #{} does not exist".format(x))  
    f.close
elif args.operation == "report":    
    today = date.today()
    with open("todo.txt","r") as f:
        lines = f.readlines()
        Pending = len(lines)
        f.close
    with open("done.txt","r") as f:
        lines = f.readlines()
        Completed = len(lines)
        f.close
    sys.stdout.write("{}//{}//{} Pending : {} Completed : {}".format(today.day,today.month,today.year,Pending,Completed))
elif args.operation == "help":
    sys.stdout.write(use)
elif args.operation == "ls":
    with(open("todo.txt","r")) as f:
        lines = f.readlines()
        count = len(lines)
        for i in range(0,count):
            count -= 1
            print("[{}] {}".format(count+1,lines[count]))