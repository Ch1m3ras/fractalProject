import turtle
import math
drawTurtle = turtle.Turtle()
drawTurtle.setheading(90)

def pythagorusFractalTree(size, turtleType, iterations, firstSquare):
    if iterations == 0:
        for x in range(0, 4):
            turtleType.forward(size)
            if firstSquare == True:
                turtleType.right(90)
            elif firstSquare == False:
                turtleType.left(90)
    else:
        for x in range(0 , 4):
            turtleType.forward(size)
            previousHeading = turtleType.heading()
            if x <= 1:
                turtleType.left(45)
                if x == 0:
                    pythagorusFractalTree(math.sqrt(2) * (size * 1/2), turtleType, (iterations - 1), True)
                elif x == 1:
                    pythagorusFractalTree(math.sqrt(2) * (size * 1/2), turtleType, (iterations - 1), False)
                turtleType.setheading(previousHeading)
            turtleType.right(90)

            
            



pythagorusFractalTree(100, drawTurtle, 2, False)

#More code do disregard to make sure VS doesn't instantaneously explode upon running it.
input()
