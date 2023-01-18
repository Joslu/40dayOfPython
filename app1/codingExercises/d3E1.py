user_country = input("What's your country?: ").strip()


match user_country:

    case 'USA':
        print('Hello')

    case 'GERMANY':
        print('Hallo')

    case 'INDIA':
        print('Namaste')