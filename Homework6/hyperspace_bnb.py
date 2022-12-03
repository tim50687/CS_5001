"""
    CS 5001
    2022 Fall
    Jen Ting Huang
    Homework 6: Program 2 - Hyperspace BnB
"""


def load_travelers(travelers_file_name):
    """
    Function --
        Collect the aliens' data, and sort it
        to a dictionary
    Parameter --
        travelers_file_name: data of each traveler
    Return --
        Dictionary:
        ex.
        {ID : {"Name": xxxxx , "Credit": xxxxxx}}
    """
    try:
        travelers_data = {}
        with open(travelers_file_name, "r", encoding="utf-8") as f:
            for line in f:
                # Clean the data
                each_line = line.strip("\n").split("@")
                # Create dictionary,
                # ex. {ID : {"Name": xxxxx , "Credit": xxxxxx}}
                travelers_data[each_line[1]] = {
                    "Name": each_line[0],
                    "Credit": each_line[2],
                }
        return travelers_data
    except FileNotFoundError:
        print("Cannot find your file")
    except PermissionError:
        print("Oops you don't have the access right to this file!")


def process_requests(travelers, request_file_name):
    """
    Function --
        Based on the request_file_name, create (or update) booking
        file that record all of the successful request. Otherwise,
        do not create (or modified) booking file.
    Parameter --
        travelers: sorted travelers' data
        request_file_name: booking request file
    Return --
        None
    """
    try:
        fee = 500  # BnB Fee
        with open(request_file_name, "r", encoding="utf-8") as f:
            # Create a list stores the week is successful booked
            booked_week = []
            for line in f:  # Processing the requests sequentially
                # Read the request
                # and store alien's data to varaibles
                id = line.strip("\n").split()[0]
                week = line.strip("\n").split()[1]
                name = travelers[id]["Name"]
                credit = int(travelers[id]["Credit"])
                # If alien has enought credit and requested week
                # was not booked, then process the request, write
                # it in bookings.txt
                if week not in booked_week and credit >= fee:
                    with open("bookings.txt", "a", encoding="utf-8") as f:
                        f.write(f"{week} - {id} - {name}\n")
                    booked_week.append(week)
                    travelers[id]["Credit"] = str(credit - 500)
                else:
                    continue
    except FileNotFoundError:
        print("Cannot find your file")
    except PermissionError:
        print("Oops you don't have the access right to this file!")


def main():
    print(load_travelers("travelers.txt"))
    process_requests(load_travelers("travelers.txt"), "requests.txt")


if __name__ == "__main__":
    main()
