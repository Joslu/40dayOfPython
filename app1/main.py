
while True:
    # Get user input and strip space chars from it
    user_option = input('Do you want to add, show, edit, complete,  or exit?: ')
    user_option = user_option.strip()

    match user_option:
        # Check if user asction is 'add'
        case 'add':
            todo = input("Enter a new todo: ") + '\n'

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        
        case 'show':

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            for index, todo in enumerate(todos):
                todo.strip('\n')
                print(f'{index + 1 }-{todo}')

        case 'exit':
            break

        case 'edit':
            print('Editing zone')
            number = int(input("Number of the todo to edit?: "))
            number = number - 1

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Number ot the todo to complete: "))

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from list"
            print(message)

        case _:
            print('You entered a unknow command')



print('Bye humans')