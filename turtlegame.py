import turtle
import time
import random
WIDTH, HEIGHT = 300, 300
COLORS = ['red', 'blue', 'orange', 'green', 'yellow']
def get_no_of_turtles ():
    number = 0
    while True:
        number = input("enter the number of turtles from 2 to 5: ")
        if number.isdigit():
            number = int(number)
        else:
            print("the input is not numeric")
            continue

        if 2<= number <=5:
            return number
        else:
            print("not a valid number. try again.")


def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors)+1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles



def init_turtle():

    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Game")

racers = get_no_of_turtles()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print("the winner is the turtle with color: ", winner)
time.sleep(25)