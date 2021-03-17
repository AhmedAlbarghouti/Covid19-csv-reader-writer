import ControllerC


# By Ahmed Albarghouti

def print_menu():
    """Prints Menu Options"""
    print("\n\n")
    print("Please choose one of the following menu options:")
    print("1.Reload the data from the dataset")
    print("2.Save the data from memory to a CSV file")
    print("3.Select and display either one record, or display multiple records")
    print("4.Create a new record and store it")
    print("5.Select and edit a record")
    print("6.Select and delete a record")
    print("7.Exit program")


def view_reload_data():
    """calls load_data() function from ControllerC and stores the returning to send it to print_records() to be
    printed """
    records = ControllerC.load_data()
    print_records(records)


def print_records(records):
    """"Prints every obj within the list that is passed to this function using for each loop"""

    objcount = 1
    for obj in records:
        print(objcount, ". ", obj.pruid, obj.prname, obj.prnameFr, obj.date, obj.numconf, obj.numprob, obj.numdeaths,
              obj.numtotal, obj.numtoday, obj.ratetotal)
        objcount += 1


def view_save_data():
    """"Asks user for filename then calls save_data() passing to it the file name"""
    print("Enter the file name: ")
    name = input()
    print(ControllerC.save_data(name))


def view_display_record():
    """"prints more specific options of display to the user to choose then takes the information required to find
    these specific records and passes them to their respective functions in ControllerC

    if user inputs a letter then a ValueError is handled and an error message is printed.
    By Ahmed Albarghouti |
    """

    try:
        print("Choose one of the following options to display record/s")
        print("1.Display a record with a specific unique province id.")
        print("2.Display a record on a specific date.")
        print("3.Both.Display a record with a specific unique province id on a specific date.")
        print("4.Display all available records.")
        choice = input()
        if int(choice) == 1:
            print("Please enter the province unique id: ")
            pruid = input()
            print_records(ControllerC.display_record_with_id(pruid))

        elif int(choice) == 2:
            print("Please enter the date using the following format: YYYY-MM-DD")
            date = input()
            print_records(ControllerC.display_record_with_date(date))

        elif int(choice) == 3:
            print("Please enter the province unique id: ")
            pruid = input()
            print("Please enter the date using the following format: YYYY-MM-DD")
            date = input()
            print_records(ControllerC.display_record_with_iddate(pruid, date))

        elif int(choice) == 4:
            print_records(ControllerC.records)
    except ValueError:
        print("Error! Please don't enter any letters.")


def view_create_record():
    """"Requests the information required to create a new Record object and passes it to create_record()"""

    print("Enter a unique province id: ")
    pruid = input()
    print("Enter the province name in english: ")
    prname = input()
    print("Enter the province name in french: ")
    prnameFr = input()
    print("Enter a date using the following format: YYYY-MM-DD")
    date = input()
    print("Enter number of confirmed cases: ")
    numconf = input()
    print("Enter number of probable cases: ")
    numprob = input()
    print("Enter number of deaths: ")
    numdeaths = input()
    numtotal = numprob + numconf
    print("Enter number of new cases since the last record:")
    numtoday = input()
    print("Enter number of Case rate per one hundred thousand population")
    ratetotal = input()
    print(ControllerC.create_record(pruid, prname, prnameFr, date, numconf, numprob, numdeaths, numtotal, numtoday,
                                    ratetotal))


def view_edit_record():
    """asks user for id & date to check if the record exists. if the record exists the function will offer the user 5
    options of editable attributes to choose to edit

     if user inputs a letter then a ValueError is handled and an error message is printed.
    By Ahmed Albarghouti |
    """
    print("Please enter the province unique id: ")
    pruid = input()
    print("Please enter the date using the following format: YYYY-MM-DD")
    date = input()
    if len(ControllerC.display_record_with_iddate(pruid, date)) == 0:
        print("Error!Record not found!")
    else:
        print_records(ControllerC.display_record_with_iddate(pruid, date))
        print("Choose from the following options which attribute of this record ^^ you want to change: ")
        print("1.numconf.")
        print("2.numprob.")
        print("3.numdeaths.")
        print("4.numtoday.")
        print("5.ratetotal.")
        try:
            choice = input()
            if int(choice) == 1:
                print("Enter the new numconf: ")
                numconf = input()
                print(ControllerC.edit_record(pruid, date, "numconf", numconf))
            elif int(choice) == 2:
                print("Enter the new numprob: ")
                numprob = input()
                print(ControllerC.edit_record(pruid, date, "numprob", numprob))
            elif int(choice) == 3:
                print("Enter the new numdeaths: ")
                numdeaths = input()
                print(ControllerC.edit_record(pruid, date, "numdeaths", numdeaths))
            elif int(choice) == 4:
                print("Enter the new numtoday: ")
                numtoday = input()
                print(ControllerC.edit_record(pruid, date, "numtoday", numtoday))
            elif int(choice) == 5:
                print("Enter the new ratetotal: ")
                ratetotal = input()
                print(ControllerC.edit_record(pruid, date, "ratetotal", ratetotal))
        except ValueError:
            print("Error! Please don't enter any letters.")


def view_delete_record():
    """asks user for id & date to check if the record exists. if the record exists the function will call
    delete_record() """

    print("Please enter the province unique id: ")
    pruid = input()
    print("Please enter the date using the following format: YYYY-MM-DD")
    date = input()
    if len(ControllerC.display_record_with_iddate(pruid, date)) == 0:
        print("Error!Record not found!")
    else:
        print(ControllerC.delete_record(pruid, date))


def launch():
    """"On launch the program will call view_reload_data() which will result in reading the first 100 rows of the csv
    file and storing them. calls the print_menu() to print the options for the user to choose. then the function will
    call different view fucntions depending on what the user inputs

    if user inputs a letter then a ValueError is handled and an error message is printed.
    By Ahmed Albarghouti |
    """
    # Read first 100 dataset records
    view_reload_data()
    while True:
        try:
            print_menu()
            check = input()

            if int(check) == 1:
                view_reload_data()

            elif int(check) == 2:
                view_save_data()

            elif int(check) == 3:
                view_display_record()

            elif int(check) == 4:
                view_create_record()

            elif int(check) == 5:
                view_edit_record()

            elif int(check) == 6:
                view_delete_record()

            elif int(check) == 7:
                print("Exiting.....")
                quit()

        except ValueError:
            print("Error! Please don't enter any letters.")
