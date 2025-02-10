import csv



# grab jobs from that one client
def get_by_client(client):
    all_jobs = read_csv()
# display_all_totals() in functions.py
# display_range_totals() in functions.py
# display_x_days_totals() in functions.py
    client_jobs = list(filter(lambda row: row['client'] == client, all_jobs))
    return client_jobs


class MenuOptionError(Exception):
    """Raised when an invalid menu option is used"""
    pass

# used in the menus.py script
def format_error(error_message):
    print("\n#### ERROR ####")
    print(error_message)
    print("###############\n")


def list_clients():
    data = read_csv()
    print("Here is a list of clients that exist in the tracker")
    clients = {job['client'] for job in data}
    for client in clients:
        print(client)


def return_clients():
    data = read_csv()
    clients = {job['client'] for job in data}
    return clients


def read_csv():
    data = []
    with open('data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            data.append({
                'client': row['client'],
                'description': row['description'],
                'start_time': row['start_time'],
                'end_time': row['end_time'],
            })
    return data

# function imported in the menus.py scirpt. and called within the stop_tracking_menu function as a loop
def check_if_job_running():
    with open('data.csv', 'r') as csvfile:
        last_line = csvfile.readlines()[-1]
        last_character = last_line[-1]
        return last_character == ','


def back_to_main_menu():
    input("Press any key to return to main menu...")

