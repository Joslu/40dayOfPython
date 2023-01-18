todos = []

while True:
    user_option = input('Do you want to add or show?: ')
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

        case _:
            print('You entered a unknow command')



print('Bye humans')