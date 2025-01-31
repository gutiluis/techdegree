# main file
import csv
import menus


if __name__ == '__main__':
    PEOPLE = []
    print("WELCOME TO THE BIRTHDAY DATABASE APP")
    print("Loading data...")
    # run a csv file. and load data into the PEOPLE variable
    with open('birthdays.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            PEOPLE.append({
                'name': row['name'],
                'birthday': row['birthday']
            })
            # present a menu choice to the user
    menu_choice = 0
    while menu_choice != 4: # input
        menu_choice = menus.main_menu()
        if menu_choice == 1: # input
            menus.upcoming_birthdays_menu(PEOPLE)
        if menu_choice == 2: #input
            menus.check_ages_menu(PEOPLE)
        if menu_choice == 3: #input
            menus.age_difference_menu(PEOPLE)
    print("Have a great day!")
