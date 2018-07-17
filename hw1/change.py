def main():
    print("Change Counter")
    owed=eval(input("Please enter the amount of change owed:"))
    quarters=0
    dimes=0
    nickels=0
    pennies=0
    while owed>=0.25:
            owed=owed-0.25
            quarters=quarters+1

    while owed>=0.10:
            owed=owed-0.10
            dimes=dimes+1

    while owed>=0.05:
        owed=owed-0.05
        nickels=nickels+1
    while owed>=0.01:
        owed=owed-0.01
        pennies=pennies+1


    
    print("Your change is",quarters,"Quarters",dimes,"dimes",nickels,"nickels and",pennies,"pennies.")

main()