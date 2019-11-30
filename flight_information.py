import csv
'''
Input departure, arrival, non-stop or not, sort according to price or not(for non-stop flights)
Output flight info: flight_number, departure_city, departure_airport, arrival_city, arrival_airport, departure_time, arrival_time, arrival_day, price
Flights includes departure from Toronto to Calgary, Charlottetown, Edmonton, Fredericton, Halifax, Montreal, Ottawa, Quebec City, Regina, St.John's, Vancouver, Victoria, Winnipeg and the return flights.


'''
# the code for def read_csv are from lab8
def read_csv():
    #Found error when decoding: 'utf-8' codec can't decode byte 0x8e in position 4060: invalid start byte
    #reason: french characters in the data file
    #used code (encoding='latin1') from https://stackoverflow.com/questions/49898909/reading-a-file-with-french-characters-in-python
    FILE_NAME = "flight_info.csv"
    with open(FILE_NAME, encoding='latin1') as reader_file:
        reader = csv.reader(reader_file)
        data = list(reader)
    return (data[0], data[1:])

departure_city = input("Where are you departure from? Please enter the name of the city you are leaving. \n")
#in case of user enter city name with first letter not capitalized https://www.geeksforgeeks.org/string-capitalize-python/
departure_city = departure_city.capitalize()
#in case of user include space in input https://www.journaldev.com/23763/python-remove-spaces-from-string
departure_city = ''.join(departure_city.split())
#in case of user input french character https://www.journaldev.com/23763/python-remove-spaces-from-string
departure_city = departure_city.replace("é", "e")
arrival_city = input("Where is your destination? Please enter the name of the city you are heading to. \n")
arrival_city = arrival_city.capitalize()
arrival_city = ''.join(arrival_city.split())
arrival_city = arrival_city.replace("é", "e")
direction = input("Do you want a non-stop flight or not? Please enter Yes or No. \n")
direction = direction.capitalize()
need_sorted = input("Do you want searching result sorted by price low to high? Please enter Yes or No. \n")
need_sorted = need_sorted.capitalize()


def timetable(direction, departure_city, arrival_city, need_sorted):


    print("\n======================= Searching Results =======================\n")

    #output non-stop flight info
    if(direction == "Yes"):
        database = read_csv()[1]
        check = 0
        flight_info_sorted = []
        for flight_info in database:
            #for non-stop flights, the departure and arrvial city should be same as the input
            if flight_info[2] == departure_city and flight_info[3] == arrival_city:
                # Check if the user want to sort by price low to high
                if (need_sorted == "Yes"):
                    # Current sorted flight info list is empty
                    if len(flight_info_sorted) == 0:
                        flight_info_sorted.append(flight_info)
                    # Current sorted flight info list contains only one record
                    elif len(flight_info_sorted) == 1:
                        if flight_info[9] <= flight_info_sorted[0][9]:
                            flight_info_sorted.insert(0, flight_info)
                        else:
                            flight_info_sorted.append(flight_info)
                    # Current sorted flight info list contains more than one record
                    else:
                        if flight_info[9] <= flight_info_sorted[0][9]:
                            flight_info_sorted.insert(0, flight_info)
                        elif flight_info[9] > flight_info_sorted[len(flight_info_sorted)-1][9]:
                            flight_info_sorted.append(flight_info)
                        else:
                            # Go through sorted flight info list to find the proper position for inserting current satisfied flight info
                            i = 0
                            inserted = False
                            while (i<(len(flight_info_sorted)-1)) and (inserted == False):
                                if flight_info_sorted[i][9] <= flight_info[9] <= flight_info_sorted[i+1][9]:
                                    flight_info_sorted.insert(i+1, flight_info)
                                    inserted = True
                                i = i + 1
                else:
                    flight_info_sorted.append(flight_info)
                check = check + 1
        if(check == 0):
            print("No direct flight between the two cities entered.")
        else:
            for flight_info in flight_info_sorted:
                print("AC" + flight_info[0] + ": " + flight_info[2] + "(" + flight_info[1] + ")" + " -> " + flight_info[3] + "(" + flight_info[4] + ") " + flight_info[5][1:3] + ":" + flight_info[5][3:5] + " - " + flight_info[6][1:3] + ":" + flight_info[6][3:5] + " +" + str(flight_info[7]) + "days" + " $" + str(flight_info[9]))

    else:
    #output 1 stop flights info
        database = read_csv()[1]
        departure = []
        arrival = []
        #find all flights with departure city same as input and put them in list departure_city
        check = 0
        for flight_info in database:
            if flight_info[2] == departure_city:
                departure.append(flight_info)
            #find all flights with arrival city same as input and put them in list arrival
            elif flight_info[3] == arrival_city:
                arrival.append(flight_info)
        #compare one flight from departure with one flight from arrival
        #when flight1 arrival matches flight2 departure and the flight2 departure time > flight1 arrival time, print both flights info
        for flight1 in departure:
            for flight2 in arrival:
                if flight1[3] == flight2[2] and int(flight2[5][1:]) > int(flight1[6][1:]):
                    print("AC" + flight1[0] + " -> " + "AC" + flight2[0] + ": " + flight1[2] + "(" + flight1[1] + ")" + " -> " + flight1[3] + "(" + flight2[1] + ")" + " -> " + flight2[3] + "(" + flight2[4] + ")" + " local time for each city: " + flight1[5][1:3] + ":" + flight1[5][3:5] + " - " + flight2[6][1:3] + ":" + flight2[6][3:5] + " +" + str(int(flight1[7])+int(flight2[7])) + "days" + " $" + str(int(flight1[9])+int(flight2[9])))
                    check = check + 1

                elif flight1[3] == flight2[2] and int(flight2[5][1:]) <= int(flight1[6][1:]):
                    print("AC" + flight1[0] + " -> " + "AC" + flight2[0] + ": " + flight1[2] + "(" + flight1[1] + ")" + " -> " + flight1[3] + "(" + flight2[1] + ")" + " -> " + flight2[3] + "(" + flight2[4] + ")" + " local time for each city: " + flight1[5][1:3] + ":" + flight1[5][3:5] + " - " + flight2[6][1:3] + ":" + flight2[6][3:5] + " +" + str(1+int(flight1[7])+int(flight2[7])) + "days" + " $" + str(int(flight1[9])+int(flight2[9])))
                    check = check + 1

        if(check == 0):
            print("No one-stop flight between the two cities entered.")


timetable(direction, departure_city, arrival_city, need_sorted)

'''
    # Test reading CSV file
    print("\nTest reading CSV file:\n")
    csv_data = read_csv()
    print(csv_data)
    # Test Timetable()
    print("\nTest stop flights:\n")
    timetable("Nooooooo", "Toronto", "Halifax")
    print("\nTest non-stop flights:\n")
    timetable("Yes", "Toronto", "Halifax")
'''
