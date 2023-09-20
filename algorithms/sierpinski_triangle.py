"""
Draws sierpiński triangle fractal using turtle library
"""
import turtle


def draw_triangle(t, length):
    """
    Draws triangle with given length
    :param t: turtle
    :param length: length of triangle side
    :return: None
    """
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)


def sierpinski(t, length, depth):
    """
    Draws sierpiński triangle fractal
    :param t: turtle
    :param length: length of triangle side
    :param depth: depth of fractal
    :return: None
    """
    if depth == 0:
        draw_triangle(t, length)
    else:
        sierpinski(t, length / 2, depth - 1)
        t.forward(length)
        t.left(120)
        sierpinski(t, length / 2, depth - 1)
        t.forward(length)
        t.left(120)
        sierpinski(t, length / 2, depth - 1)
        t.forward(length)
        t.left(120)


def main():
    """
    Main function
    :return: None
    """
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.pensize(2)
    t.speed(0)
    t.color("black")

    sierpinski(t, 300, 5)

    window.exitonclick()


if __name__ == "__main__":
    main()