def main():
    print("This program will print out a grade from a score between 0-5.")
    score=int(input("Insert a score between 0-5 to receieve the corresponding grade (0=F,1=F,2=D,3=C, 4=B, and 5=A"))
    if score==0 or score==1:
        print("Your grade is an F")
    elif score==2:
        print("Your grade is a D")
    elif score==3:
        print("Your grade is a C")
    elif score==4:
        print("Your grade is a B")
    elif score==5:
        print("Your grade is a A")
    else:
        print("That score does not have a corresponding grade")
main()