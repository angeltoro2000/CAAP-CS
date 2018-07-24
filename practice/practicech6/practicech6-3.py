import math

def sphereArea(radius):
    formula=4*math.pi*radius**2
    print(formula)

def sphereVolume(radius):
    formula=(4/3)*math.pi*radius**3
    print(formula)



def main():
    inputforarea=eval(input("What is the radius of the sphere you want to find the surface area for?"))
    sphereArea(inputforarea)
    inputforvolume = eval(input("What is the radius of the sphere you want to find the volume for?"))
    sphereVolume(inputforvolume)
main()