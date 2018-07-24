def sumN(n):

    sum=0

    for i in range(n+1):
        sum += i
    print(sum)
    return sum

def sumNCubes(n):
    sum=0
    for i in range(n+1):
        sum +=i*i*i
    print(sum)
    return sum

def main():
    nsetto=int(input("Up to what natural number will you like to add that natural number and the previous natural numbers"))
    sumN(nsetto)
    n2setto = int(input("Up to what natural number will you like to add that cubes of that number and the previous natural numbers"))
    sumNCubes(n2setto)

main()










