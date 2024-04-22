import turtle
drawTurtle = turtle.Turtle()

def pythagorusFractalTree(size, turtleType, iterations):
    makeSquare(size, turtleType)

def makeSquare(length, turtleType):
    for x in range(0, 4):
        turtleType.forward(length)
        turtleType.right(90)

pythagorusFractalTree(100, drawTurtle, 5)

#More code do disregard to make sure VS doesn't instantaneously explode upon running it.
input()