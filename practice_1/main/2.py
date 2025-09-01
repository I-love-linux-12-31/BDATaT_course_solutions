from math import sqrt, pi


AVAILABLE_FIGURES = ["triangle", "rectangle", "circle"]


def get_rectangle_area(a, b):
    return a * b

def get_triangle_area(a, b, c):
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))

def get_square_area(r):
    return pi * r ** 2


def triangle_dialog():
    a, b, c = map(float, input("Enter sides of triangle in one line:").split())
    result = get_triangle_area(a, b, c)
    print("The area of the triangle is:", result)
    return result

def rectangle_dialog():
    a, b = map(float, input("Enter sides of rectangle in one line:").split())
    result = get_rectangle_area(a, b)
    print("The area of the rectangle is :", result)
    return result

def circle_dialog():
    r = float(input("Enter radius of circle: "))
    result = get_square_area(r)
    print("The area of the circle is:", result)
    return result

def main():
    result = dict()
    for _ in range(3):
        figure = input("Which figure do you want to find area (\"triangle\", \"rectangle\", \"circle\")? ")
        match figure:
            case "triangle":
                result["triangle"] = triangle_dialog()
            case "rectangle":
                result["rectangle"] = rectangle_dialog()
            case "circle":
                result["circle"] = circle_dialog()
            case _:
                print("Invalid choice.")
                return

    print("-=- " * 12)
    print(result)

if __name__ == '__main__':
    main()
