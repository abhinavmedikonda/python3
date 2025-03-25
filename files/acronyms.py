def find_acronym():
    lookup = input('what acronym would you like to look up: \n')

    found = False
    try:
        with open('acronyms.txt') as file:
            for item in file:
                if lookup in item:
                    print(item)
                    found = True
                    break
    except:
        print('file error')
        return

    if not found:
        print('acronym does not exist')

def add_acronym():
    acronym = input('what acronym do you want to add: ')
    full_form = input('full form of the acronym: ')

    with open('acronyms.txt', 'a') as file:
        file.write(f'{acronym} - {full_form}\n')

def main():
    choice = input('Do you want to find(F) or add(A) an acronym?\n')
    if(choice == 'F'):
        find_acronym()
    elif(choice == 'A'):
        add_acronym()

main()
