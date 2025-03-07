
while True :
    user_action = input("Type add or show or edit or complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("enter todo : ")+ "\n"
            # file = open('todos.txt','r')
            # todos = file.readlines()
            # file.close() 
            with open('todos.txt','r') as file :
                todos = file.readlines()


            todos.append(todo)


            # file = open("todos.txt",'w')
            # file.writelines(todos)
            # file.close()
            with open('todos.txt','w') as file :
                file.writelines(todos)

        case 'show':
            file = open('todos.txt','r')
            todos = file.readlines()
            file.close()
            for index,item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit : "))
            number = number -1

            with open('todos.txt','r') as file :
                todos = file.readlines()

            print(todos[number])
            new_todo = input("Enter old todo : ")
            todos[number] = new_todo +'\n'

            with open('todos.txt','w') as file :
                file.writelines(todos)
        
        case 'complete':
            number = int(input("Enter the index"))

            with open('todos.txt','r') as file :
                todos = file.readlines()

            todos.pop(number -1)

            with open('todos.txt','w') as file :
                file.writelines(todos)

        case 'exit':
            break

print("byeee")