def validYr(year):
    if 1900 <= year <= 2099:
        return "valid input"



def main():
    # Program purpose:
    print(
        "This program inputs a year, verifies that it is in the proper range, and then prints out the date of Easter that year")

    # Prompt for year:
    year = eval(input("What is the year (1900-2099)? "))

    # If valid year, calculate and output Easter date:
    if validYr(year) == "valid input":
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        day = 22 + d + e
        if year == 1954:
            if day > 31:
                day = day - 38
                print("Easter in {0} is April {1}.".format(year, day))
            else:
                print("Easter in {0} is March {1}.".format(year, day))
        elif year == 1981:
            if day > 31:
                day = day - 38
                print("Easter in {0} is April {1}.".format(year, day))
            else:
                print("Easter in {0} is March {1}.".format(year, day))
        elif year == 2049:
            if day > 31:
                day = day - 38
                print("Easter in {0} is April {1}.".format(year, day))
            else:
                print("Easter in {0} is March {1}.".format(year, day))
        elif year == 2076:
            if day > 31:
                day = day - 38
                print("Easter in {0} is April {1}.".format(year, day))
            else:
                print("Easter in {0} is March {1}.".format(year, day))
        elif day > 31:
            day = day - 31
            print("Easter in {0} is April {1}.".format(year, day))
        else:
            print("Easter in {0} is March {1}.".format(year, day))
    else:
        print("Invalid Year.")


main()

