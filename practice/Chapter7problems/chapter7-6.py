def main():
    print("This program will calculate whether your speed is legal or determine the fine if it's not legal in Podunksville")

    speedlim=(int(input("What is the speed limit: ")))

    speed=(int(input("What is your speed: ")))

    if speed<speedlim:
        print("This speed is legal")
    elif speed-90<speedlim:
        fine=50+5(speed-speedlim)
        print("This speed is illegal. Your fine is ",fine)

    elif speed-90>speedlim:

        fine=50+5(speed-speedlim)+200
        print("This speed is illegal. Your fine is", fine)
#I'm receiving an error but unsure why

main()


