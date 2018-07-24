# exercise 2 from chapter 3
# function for pizza area and one for cost per square inch

import math


def areaofpizza(d):
    formula = math.pi * (d * 2) ** 2

    return formula


def costpersquareinch(p):
    formula = areaofpizza(d) / p
    return formula


def main():
    areaofpizza(4)
    costpersquareinch(3)

    print("The price of each square inch of pizza is", costpersquareinch(p))


main()
