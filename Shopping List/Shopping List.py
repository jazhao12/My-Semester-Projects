#James Zhao
#Jan 23
#Period 7
#Shopping List


#Initialize
shopping_list = []

#Functions
def to_do_list():
    global shopping_list
    print('Welcome to your to-do list.')
    print('This to-do list will specifically be for your shopping.')
    while True:
        print('''\n
1. View the current to-do list
2. Add an item to the to-do list
3. Remove a task from the to-do list
4. Sort the list alphabetically
5. Count and print the # of items on the To-do List
6. Exit the program\n
''')
        option = input('What would you like to do? Enter 1-6.')

        if option == '1':
            print('Here is your shopping list:')
            print(shopping_list)

        elif option == '2':
            addition_to_list = input('What would you like to add to your shopping list?')
            addition_to_list = str(addition_to_list)
            shopping_list.append(addition_to_list)
            print('"' + str(addition_to_list) + '" has been added.')

        elif option == '3':
            try:
                removal_from_list = input('What would like to remove from your shopping list?')
                removal_from_list = str(removal_from_list)
                shopping_list.remove(removal_from_list)
                print('"' + str(removal_from_list) + '" has been removed.')
            except ValueError:
                print('"' + str(removal_from_list) + '" is not in the shopping list!')

        elif option == '4':
            shopping_list.sort()
            print('Shopping list successfully sorted alphabetically.')

        elif option == '5':
            count = len(shopping_list)
            print('There are ' + '\033[1m' + str(count) + '\033[0m' + ' items in your shopping list.')

        elif option == '6':
            print('Exiting the program...\n')
            break
        else:
            print('Invalid input. Please input "1", "2", "3", "4", "5", or "6".')
#Main
to_do_list()

