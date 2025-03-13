import sys
import os
import math


def solve_quadratic(a, b, c):
    if a == 0:
        print("Error. a cannot be 0", file=sys.stdout)
        sys.exit(1)

    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b - math.sqrt(discriminant)) / (2 * a)
        x2 = (-b + math.sqrt(discriminant)) / (2 * a)
        print(f"There are 2 roots\nx1 = {x1}\nx2 = {x2}")
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f"There are 1 roots\nx1 = {x}")
    else:
        print("There are 0 roots")
def interactive_mode():
    while True:
        try:
            a = float(input("a = "))
            if a == 0:
                raise ValueError("a cannot be 0")
            break
        except ValueError:
            print("Error. Expected a valid real number, got invalid instead", file=sys.stdout)
    
    while True:
        try:
            b = float(input("b = "))
            break
        except ValueError:
            print("Error. Expected a valid real number, got invalid instead", file=sys.stdout)
    
    while True:
        try:
            c = float(input("c = "))
            break
        except ValueError:
            print("Error. Expected a valid real number, got invalid instead", file=sys.stdout)
    
    print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")
    solve_quadratic(a, b, c)



