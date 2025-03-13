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
    print("Running in interactive mode...")
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


def file_mode(filename):
    print("Running in file mode...")
    if not os.path.exists(filename):
        print(f"file {filename} does not exist", file=sys.stdout)
        sys.exit(1)

    try:
        with open(filename, 'r') as file:
            line = file.readline().strip()
            parts = line.split()
            if len(parts) != 3:
                raise ValueError("invalid file format")

            a, b, c = map(float, parts)
            print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")
            solve_quadratic(a, b, c)
    except ValueError:
        print("invalid file format", file=sys.stdout)
        sys.exit(1)


def choose_mode():
    if len(sys.argv) == 1:
        interactive_mode()
    elif len(sys.argv) == 2:
        file_mode(sys.argv[1])
    else:
        print("Usage: ./equation [file]", file=sys.stdout)
        sys.exit(1)


if __name__ == "__main__":
    choose_mode()
