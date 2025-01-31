from dateutil import relativedelta # used in display_age function
# take a date string, and then a format. and turns it into a datetime object
import datetime # used in display_age function. string parse time




def upcoming_birthdays(people_list, days):
    # TODO: write code that finds all upcoming birthdays in the next 90 days
    # 90 is passed in as a parameter from menus.py
    # Template:
    # PERSON turns AGE in X days on MONTH DAY
    # PERSON turns AGE in X days on MONTH DAY
    # print("Upcoming Birthdays function")
    # print(people_list) # [{" ":" "}]
    # pass
    for person in people_list:
        format_string = "%Y-%m-%d" # use datestring to create a datetime object using string parse time
        birthday_dt = datetime.datetime.strptime(person["birthday"], format_string)

        # don't have to call it multiple times
        now = datetime.datetime.now()


        # not comming in the next 90 days
        # replace to give the year that it is today
        birthday_this_year = birthday_dt.replace(year=now.year) # replace year with now year
        # difference between this special bday
        # bday coming up this year and now
        # most recent date. either negative or positive number
        difference = birthday_this_year - now # negative bday has already passed
#        print(difference)
        turning_age = relativedelta.relativedelta(now, birthday_dt).years + 1

        if 0 < difference.days < days:
            print(f"{person["name"]} turns {turning_age} in {difference.days} days on {birthday_dt.strftime("%B %d")}")



def display_age(person):
    # TODO: write code to display the age of person
    # Template: # days between 2 dates. their bday and today
    format_string = "%Y-%m-%d" # math the string format with the proper code format
    # datetime dateime string parse time and store in a variable
    birthday_dt = datetime.datetime.strptime(person["birthday"], format_string)
    # todays date
    today = datetime.date.today()
    difference = relativedelta.relativedelta(today, birthday_dt)
#    print(difference)

    print(f"{person["name"]} is {difference.years} years, {difference.months} months, and {difference.days} days old")
#    print(person)
#    pass


def display_age_difference(people):
    # user can enter the ID of 2 people and 
    # instead of comparing someeones bday to todays date. compare the bday to another persons bday
    # TODO: write the code to display the age difference between people
    # Template:
    # PERSON is older
    # not possible to work with the datestring as a string[{"":""}].
    # make datetime objects with the [{"":""}]
    format_string = "%Y-%m-%d"
    # 2 people. datetime format
    p0_dt = datetime.datetime.strptime(people[0]["birthday"], format_string)
    p1_dt = datetime.datetime.strptime(people[1]["birthday"], format_string)

    # determine who's older
    if p0_dt < p1_dt: # if p0s datetime is earlier than p1s person datetime 
        difference = relativedelta.relativedelta(p1_dt, p0_dt) # most recent datetime
        print(f"{people[0]["name"]} is older")
    else:
        difference = relativedelta.relativedelta(p0_dt, p1_dt)
        print(f"{people[1]["name"]} is older")

    #    print(difference)

    print(f"{people[0]["name"]} and {people[1]["name"]}'s age difference is: {difference.years} years, {difference.months} months, and {difference.days} days")
    # print("Display Age Difference function")
    # print(people) # print 2 [{"":""}] of bdays
    # pass
