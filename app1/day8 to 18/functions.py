def get_todos(filepath ='todos.txt'):
    """To read the data from the file"""
    # file = open('todos.txt','r')
    # todos = file.readlines()
    # file.close() 

    with open(filepath,'r') as file :
        todos = file.readlines()
    return todos


def set_todos(todos,filepath='todos.txt'):

    """To write the data to the file"""
        
        # file = open("todos.txt",'w')
        # file.writelines(todos)
        # file.close()

    with open(filepath,'w') as file :
        file.writelines(todos)

if __name__ == "__main__":
    print("hello")
    print(get_todos())