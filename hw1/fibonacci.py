import math
def main():
    print("This program will be able to compute the nth number of the Fibonacci sequence.")
    whichnumber=int(input("Which nth term of the fibonacci sequence are you trying to find. "))
    fib=round(int((1+math.sqrt(5))**whichnumber-(1-math.sqrt(5))**whichnumber)/(2**whichnumber*math.sqrt(5)))


    print(fib)
main()
#I received help from Tina and Sadrac in finding a formual that works


