import csv

from ModelC import Record
"global list variable"
records = []


def load_data():
    """"Clears records list.
        Opens file ,reads file, creates a Record object with the information
       provided by each row and appends it within records list and finally returns records with the added Record objects

         If file not found then a FileNotFoundError is handled and an error message is printed.
         By Ahmed Albarghouti
        """
    records.clear()
    try:
        with open('covid19-download.csv') as file:
            reader = csv.DictReader(file)
            count = 0

            for row in reader:

                records.append(
                    Record(row["pruid"], row["prname"], row["prnameFR"], row["date"], row["numconf"], row
                    ["numprob"], row["numdeaths"], row["numtotal"], row["numtoday"], row["ratetotal"]))

                if count == 99:
                    break

                count += 1

    except FileNotFoundError:
        print("File not found!!")
    return records


def display_record_with_id(pruid):
    """"Creates a new list (answers) then loops through the records list appending objects from the records list to
    answers if the date is identical. returns answers """
    answers = []
    for obj in records:
        if obj.pruid == pruid:
            answers.append(obj)

    return answers


def display_record_with_date(date):
    """"Creates a new list (answers) then loops through the records list appending objects from the records list to
        answers if the date is identical. returns answers
        By Ahmed Albarghouti """
    answers = []
    for obj in records:
        if obj.date == date:
            answers.append(obj)

    return answers


def display_record_with_iddate(pruid, date):
    """"Creates a new list (answers) then loops through the records list appending objects from the records list to
        answers if the province id and date are identical. returns answers """
    answers = []
    for obj in records:
        if obj.pruid == pruid:
            if obj.date == date:
                answers.append(obj)

    return answers


def create_record(pruid, prname, prnameFr, date, numconf, numprob, numdeaths, numtotal, numtoday, ratetotal):
    """"Creates a new Record object using the passed arguments and appends the new object to the records list"""
    records.append(
        Record(pruid, prname, prnameFr, date, numconf, numprob, numdeaths, numtotal, numtoday, ratetotal))
    return "Record created successfully!"


def edit_record(pruid, date, attribute, change):
    """"loops through the records list. if the province id and date match the looped object then the object's
    argument will get edited based on what the user chose to edit
    By Ahmed Albarghouti """
    for obj in records:
        if obj.pruid == pruid:
            if obj.date == date:
                if attribute == "numconf":
                    obj.set_numconf(change)
                elif attribute == "numprob":
                    obj.set_numprob(change)
                elif attribute == "numdeaths":
                    obj.set_numdeaths(change)
                elif attribute == "numtoday":
                    obj.set_numtoday(change)
                elif attribute == "ratetotal":
                    obj.set_ratetotal(change)
    return "Record edited successfully!"


def delete_record(pruid, date):
    """"Loops through the records until provence id and data matches then proceeds to remove said object from the
    records list """
    for obj in records:
        if obj.pruid == pruid:
            if obj.date == date:
                records.remove(obj)
    return "Record deleted successfully!"


def save_data(name):
    """"Writes a new file using DictWriter making sure to overwrite the file if it already exists
    By Ahmed Albarghouti
    """
    with open(name, 'w') as csv_file:
        attributes = ['pruid', 'prname', 'prnameFr', 'date', 'numconf', 'numprob', 'numdeaths', 'numtotal', 'numtoday',
                      'ratetotal']
        writer = csv.DictWriter(csv_file, attributes)
        writer.writeheader()
        for record in records:
            writer.writerow(
                {'pruid': record.pruid, 'prname': record.prname, 'prnameFr': record.prnameFr, 'date': record.date,
                 'numconf': record.numconf, 'numprob': record.numprob, 'numdeaths': record.numdeaths,
                 'numtotal': record.numtotal, 'numtoday': record.numtoday, 'ratetotal': record.ratetotal})
    return "File saved successfully!"
