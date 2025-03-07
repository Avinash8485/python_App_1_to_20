todos =[]
while True :
    user_action = input("Type add or show or exit: ")

    match user_action:
        case 'add':
            todo = input("enter todo : ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break
print("byeee")

members = ["john", "sarah", "dora"]

for item in members:
    print(item.capitalize())

country = "USA"

match country:
    case 'USA'| 'United States':
        print("Hello")
    case 'Italy':
        print("Ciao")
    case 'Germany':
        print("Hallo")

