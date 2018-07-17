def main():

    print("This program will give the sum of numbers as entered by the user")
    howmany=int(input("How many numbers would you like to add?"))
    sum=0
    for i in range(howmany):
        whichones=eval(input("Select one of the numbers that you would like to add?"))
        sum=sum+whichones
    print("The addition of the",howmany,"numbers you selected is",sum)


main()
