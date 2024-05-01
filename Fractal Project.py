import turtle
import math
drawTurtle = turtle.Turtle()

def pythagorusFractalTree(size, turtleType, iterations,):
    turtleType.setheading(90)
    if iterations == 0:
        for x in range(0, 4):
            turtleType.forward(size)
            turtleType.right(90)
    else:
        for x in range(0 , 4):
            turtleType.forward(size)
            turtleType.left(30)
            pythagorusFractalTree(size * ((2 ** 1/2) / 2), turtleType, (iterations - 1))
            turtleType.left(30)



pythagorusFractalTree(100, drawTurtle, 1)

#More code do disregard to make sure VS doesn't instantaneously explode upon running it.
input()
