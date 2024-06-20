'''
ip:
queries=7
1 school
1 world
1 word
1 scholar
2 word
2 wood
3 sch

op:
insert all 1 words
True
False
True'''
def menu():
    print("\nSimple Menu:")
    print("1.insert")
    print("2.search")
    print("3.subsearch")
    print("4.exit")
    choice = input("Enter your choice (1-4): ")
    return choice
def insert():
    global m
    print("\nenter input to be inserted")
    s=input()
    m.append(s)
    
    
def search():
    print("\nenter the word to be search")
    s=input()
    if s in m:
        print(True)
    else:
        print(False)

def subsearch():
    print("\nEnter the prefix to be searched:")
    prefix = input()
    found = any(i.startswith(prefix) for i in m)
    print(found)

n=int(input())
m=[]
for i in range(n):
    choice = menu()
    if choice == '1':
        insert()
    elif choice == '2':
        search()
    elif choice == '3':
        subsearch()
    elif choice == '4':
        print("Exit")
        break
    else:
        print("Invalid choice")
