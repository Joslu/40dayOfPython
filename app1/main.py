todos = []

while True:
    user_option = input('Do you want to add, show, edit or exit?: ')
    user_option = user_option.strip()

    match user_option:

        case 'add':
            todo = input("Enter a new todo: ")
            todos.append(todo)

        case 'show':
            for i in todos:
                print(i)

        case 'exit':
            break

        case 'edit':
            print('Editing zone')
            number = int(input("Number of the todo to edit?: "))
            number = number - 1
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo

        case _:
            print('You entered a unknow command')



print('Bye humans')