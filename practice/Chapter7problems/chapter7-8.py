def main():
    print("This program will identify whether a person is eligible to be on the Senate or/ and the house of representative based on age and years of citizenship")
    age=int(input("Age: "))
    citizenshipyear=int(input("Years of citizenship"))

    if age>=30 and citizenshipyear>=9:
        print("\nYou are eligible to be in the Senate.")
    else:
        print("\nYou are not eligible to be in the Senate. ")
    if age>=25 and citizenshipyear>=7:
        print("\nYou are eligible to be in the House of Representatives.")
    else:
        print("\nYou are not eligible to be in the House of Representatives.")
main()