
def get_todos(user):
    """ Read a text file and return the list of to-do items"""
    filepath=f"{user}_todos.txt"
    try:
        with open(filepath, "r") as file_local:
            todos_local = file_local.readlines()
        return todos_local
    except FileNotFoundError:
        return []



def write_todos(todos_local, user):
    """ Write the to_do items in the text file"""
    filepath=f"{user}_todos.txt"
    with open(filepath,"w") as file_local:  # same as file=open() but better closes the file automatically even if the program stops abruptly
        file_local.writelines(todos_local)