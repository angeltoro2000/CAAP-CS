def valid(date):
    dateStr = date.split("/")
    month = eval(dateStr[0])
    day = eval(dateStr[1])
    year = eval(dateStr[2])

    month31 = [1, 3, 5, 7, 8, 10, 12]
    month30 = [4, 6, 9, 11]

    if month in month31:
        if day <= 31:
            return "Valid Date"
        else:
            return "Invalid Date"
    elif month in month30:
        if day <= 30:
            return "Valid Date"
        else:
            return "Invalid Date"
    elif month == 2:
        if year % 4 == 0:
            if year % 100 == 0 and year % 400 != 0:
                if day <= 28:
                    return "Valid Date"
                else:
                    return "Invalid Date"
            else:
                if day <= 29:
                    return "Valid Date"
                else:
                    return "Invalid Date"
        else:
            if day <= 28:
                return "Valid Date"
            else:
                return "Invalid Date"
    else:
        return "Invalid Date"


def main():
    date = input("Enter a date(mm/dd/yyyy) (If it's January, or a single digit month or day write (1, not 01)")
    print(valid(date))


main()