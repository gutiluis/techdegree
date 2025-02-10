import utils # utils.py file import
import functions # functions.py file import


def main_menu():
    try:
        print("======== MENU ========")
        print("1 - Calculate totals")
        print("2 - Start tracking")
        print("3 - Stop tracking")
        print("4 - Quit the app")
        print("======================")
        choice = input("What would you like to do? ")
        if choice not in ["1", "2", "3", "4"]:
            raise utils.MenuOptionError
        return int(choice)
    except utils.MenuOptionError:
        utils.format_error("That is not a valid menu option, please try again!")

# display all totals
# error handling
# print a second menu. calculate totals. 
def calculate_totals_menu():
    utils.list_clients()
    client = input("Which client do you want to calculate totals for? ")
    if client in utils.return_clients():
        print("======== DATE RANGE ========")
        print("1 - Enter date range")
        print("2 - Check the last X days")
        print(f"3 - Retrieve all data for {client}")
        range_choice = input("Make your choice: ")
        if range_choice == "1":
            date_range_menu(client) # call date_range_menu(client) function
        elif range_choice == "2":
            last_x_days_menu(client) # call last_x_days_menu(client) function
        elif range_choice == "3":
        # display all totals function of the functions.py import
            functions.display_all_totals(client) # functions.py
        else:
            utils.format_error("That is not a valid option.")
    else:
        utils.format_error(f"{client} is not a client in your tracker")
    utils.back_to_main_menu()


# list of date strings into display range totals
# user input a date range
def date_range_menu(client):
    print("Enter the date range in which you want to retrieve data from")
    user_input = input("Use the format [YYYY-MM-DD to YYYY-MM-DD]: ")
    try:
        split_dates = user_input.split(" to ")
        # list of date strings
        # user input date range and splits it.
        # then pass the client name and list of date strings into display range totals from the functions.py import
        functions.display_range_totals(client, split_dates) # functions.py
    except ValueError:
        utils.format_error("That's not a valid format")

# if user input last x days. menu function will be called
def last_x_days_menu(client):
    try:
        user_input = int(input(f"Retrieve data on {client} from how many days ago? "))
        # how many days they'd like to go back for, and that is passed
        # dislpay client name
        # display_x_days_totals() is a function inside the functions.py file
        functions.display_x_days_totals(client, user_input) # functions.py file
    except ValueError:
        utils.format_error("That is not a valid number")



# gather details from the user about the client and job description
# if a job is running stop it
def start_tracking_menu():
    print("=========================")
    # check_if_job_running() function from within the utils.py file import
    if utils.check_if_job_running():
        print("There is already a job being tracked. Let's stop it first.")
        print("Stopping job...")
        functions.stop_tracking()
        print("Previous job stopped")
        print("=========================")
    print("Who is the client?")
    utils.list_clients()
    client = input("Enter one of the above or a new client: ")
    description = input("Enter a short description: ")
    # functions.py file
    # start_tracking function has same parameters in the functions.py file
    functions.start_tracking(client, description) # call start_tracking() function from within the functions.py file
    print("=========================")
    utils.back_to_main_menu()


# if there isn't a job running print an error
def stop_tracking_menu():
    if utils.check_if_job_running(): # from utils.py script. call check_if_job_running function
        print("=========================")
        # functions.py file in same working directory
        functions.stop_tracking() # call stop_tracking() function
        print("=========================")
    else:
        utils.format_error("No job to stop tracking!") # from utils.py script
    utils.back_to_main_menu()
