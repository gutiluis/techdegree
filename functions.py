import csv
import utils
import datetime # used with datetime.datetime.now()
from dateutil import relativedelta



# gather details from the user about the client and job description. and then use it in the menus.py script
def start_tracking(client, description):
    print(f"Start tracking {description} for {client}")

    # TODO: Grab the current date-time object and store it as a string in start_time
    # in the format: HH:MM(AM/PM) YYYY-MM-DD
    # for example: 09:40AM 2023-08-11
    # use string format time to turn the date-time object to a string
    # hour 12 hour clock %I
    # minute %M
    # AM %p
    # YYYY %Y
    # MM %m
    # DD %d

# import datetime
    now = datetime.datetime.now()

    format_string = "%I:%M%p %Y-%m-%d"

# turn the start_time string to a start_time datet time
# (date = now, format_string)
    start_time = datetime.datetime.strftime(now, format_string)

    # ability to append all the data to a CSV file already done
    # Code to append a new job to the CSV
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', lineterminator='')
        writer.writerow([client, description, start_time, ''])


# used in the menus.py script and called in the stop_tracking_menu function
def stop_tracking():
    print("Stopping tracking")

    # TODO: Grab the current time and store it as a string in end_time
    # in the format: HH:MM(AM/PM) YYYY-MM-DD
    # for example: 09:40AM 2023-08-11

    now = datetime.datetime.now()
    format_string = "%I:%M%p %Y-%m-%d"

    end_time = datetime.datetime.strftime(now, format_string)

    # Code to append a new job to the CSV
    with open('data.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([end_time])


def display_all_totals(client):
    print(f"Calculating time spent on all jobs for {client}...")
# get_by_client from utils.py file
    client_jobs = utils.get_by_client(client)

    # TODO: List out all the different jobs, and then a total time spent
    # For example, if the user chooses Emmerton:
    # Monthly Meeting - 1 hours 0 minutes
    # Onboarding replacement - 2 hours 0 minutes
    # Follow-up questions - 0 hours 28 minutes
    # TOTAL FOR EMMERTON: 3 hours 28 minutes

    total = relativedelta.relativedelta()


# loop through the dictionaries
    for job in client_jobs: # for each job in client many jobs
        format_string = "%I:%M%p %Y-%m-%d"
        # parse datestring
        start_dt = datetime.datetime.strptime(job["start_time"], format_string)
        end_dt = datetime.datetime.strptime(job["end_time"], format_string)
        # calculate difference with start_dt and end_dt. 
        # time spent in particular job with relativedelta
        # print one relativedelta per job description
        time_spent = relativedelta.relativedelta(end_dt, start_dt)

# descrption from within the dictionary in the clients_job
        print(f"{job['description']} - {time_spent.hours} hours {time_spent.minutes} minutes")

        # add time spent to total time
        total += time_spent
        # print out job itselt
# add time spent to the total
    print(f"Total for {client}") # total is a relativedelta object
#    print(f"X hours x minutes") # acces the hours/minutes of the relativedelta object directly
    print(f"{total.hours} hours {total.minutes} minutes")


    # references
#    print(client)
    # same client_jobs from get_by_client function in utils.py import
 #   print(client_jobs) 





# when the user decides to input a date range
def display_range_totals(client, dates_str_list):
    print(f"Calculating time spent on jobs for {client} in the specified range...")
# client_jobs from get_by_client function in utils.py
# second function with the client_jobs variable in utils.py
# also used in the display_all_totals() function 
    client_jobs = utils.get_by_client(client)

# 3 client_jobs
 #   print(client_jobs)
  #  print(dates_str_list)

    # turn the dates_str_list to date times YYYY-MM-DD
    # dates_str_list contains 2 date strings in the format YYYY-MM-DD
    # TODO: turn the two date strings in dates_str_list to datetime objects and store in range_start_dt and range_end_dt

    format_string = "%Y-%m-%d"
# string parse time to parse the date yyyy-mm-dd into a datetime object
# first date string. dates string list at index 0. (first element start date, and them format_string)
#    range_start_dt = None
    range_start_dt = datetime.datetime.strptime(dates_str_list[0], format_string)
    #range_end_dt = None
# use index 1 to get the second element at index 1 YYYY-MM-DD
# turn a string into a datetime
# missing hour, minute, and seconds, will default to zero.
# for a range make sure the end date has the time. or the range will stop at the beginning of the end date. use replace(hour=23, minute=59, second=59)
# 06:00PM 2023-09-03 from onboarding replacement job
###### always set to the las second of that day [2023-09-10]
    range_end_dt = datetime.datetime.strptime(dates_str_list[1], format_string).replace(hour=23, minute=59, second=59)

# start a total to list all the different jobs, and then a total time spent
# empty relativedelta object
    total = relativedelta.relativedelta()

    # TODO: filter client_jobs to only include those within the start and end datetimes
    # loop to filter the dictionary
# test whether the end time fails within the range
    for job in client_jobs:
# string parse time
        format_string_dt = "%I:%M%p %Y-%m-%d"
#turn end time to a datetime. 
# range date time. target jobs that fall inside of the range
        job_end_dt = datetime.datetime.strptime(job['end_time'], format_string_dt)
# smaller date time is an earlier date time
# needs to evaluate to true. to fall inside the range needed
        if range_end_dt > job_end_dt > range_start_dt: # larger date time is a later date time
# turn job start into a date time
# calculate the time difference between it
# get start time as date times
            job_start_dt = datetime.datetime.strptime(job['start_time'], format_string_dt)
# calculate the difference
            time_spent = relativedelta.relativedelta(job_end_dt, job_start_dt)
#            print(time_spent)


    # TODO: List out all the different jobs, and then a total time spent - just like display_all_totals
# print the description in hours
            print(f"{job['description']} - {time_spent.hours} hours {time_spent.minutes} minutes")

# add to that total time spent
# start a total in the display_range_totals() function before/outside the for loop
            total += time_spent
# print total time spent 
    print(f"Total for {client}")
# print final totals
# it can print more than one job within the date range
    print(f"{total.hours} hours {total.minutes} minutes")


# days is an integer. go back in time to find the starting datetime.
# use days with relativedelta to go back in time an integer/determined number of days
# user enters a day in which they wan to go back in
def display_x_days_totals(client, days):
    print(f"Calculating time spent on jobs for {client} in the last {days} days...")
# utils.py script in same working directory
    client_jobs = utils.get_by_client(client)

    # TODO: determine the start and end datetimes for this range
    go_back = relativedelta.relativedelta(days=days)
    # ex: go back 5 days. todays date and minus that many days
#    range_start_dt = None
    range_start_dt = datetime.datetime.now() - go_back


#    range_end_dt = None
    range_end_dt = datetime.datetime.now()
#    print(range_start_dt)
 #   print(range_end_dt)

# use for loops or comprehensions to filter
    # TODO: filter and display client_jobs to only include those with the start and end datetimes
# use for dates
    total = relativedelta.relativedelta()
# use to filter
    for job in client_jobs:
    # end time is a key in the dictionary
        job_end_dt = datetime.datetime.strptime(job['end_time'], "%I:%M%p %Y-%m-%d")
        if range_end_dt > job_end_dt > range_start_dt:
            job_start_dt = datetime.datetime.strptime(job['start_time'], "%I:%M%p %Y-%m-%d")
            time_spent = relativedelta.relativedelta(job_end_dt, job_start_dt)

            print(f"{job['description']} - {time_spent.hours} hours {time_spent.minutes} minutes")

            total += time_spent

    print(f"Total for {client}")
    print(f"{total.hours} hours {total.minutes} minutes")
