def main():
    print("This program will Classify freshman, sophomores, juniors and senior s based on credits.")
    year=int(input("How many credits has this student earned: "))
    if year<7:
        print("This student is a freshman")
    elif year<16:
        print("This student is a sophomore")
    elif year<26:
        print("This student is a junior")
    else:
        print("This student is a senior")

main()

