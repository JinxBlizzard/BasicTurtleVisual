import turtle as t
import random
import time

WIDTH, HEIGHT = 400, 400
COLORS = ['red', 'blue', 'green', 'pink', 'orange', 'brown', 'cyan', 'lavender', 'violet', 'crimson']


def get_input():
    num_racers = 0
    while True:
        num_racers = input("Enter the number of racers (2, 10): ")
        if num_racers.isnumeric():
            num_racers = int(num_racers)
        else:
            print("Not a valid input. Try Again!!")
            continue

        if 2 <= num_racers <= 10:
            return num_racers
        else:
            print("Numbers should be in permissible range. Try Again!!")
            continue


def create_turtle(colors):
    racers = []
    spc = int(WIDTH // (len(colors) + 1))
    for i, clr in enumerate(colors):
        racer = t.Turtle()
        racer.color(clr)
        racer.shape('turtle')
        racer.penup()
        racer.left(90)
        racer.setpos(-WIDTH // 2 + (i + 1) * spc, -HEIGHT // 2 + 30)
        racer.pendown()
        racers.append(racer)

    return racers


def return_winner(racers, colors):
    while True:
        for idx, racer in enumerate(racers):
            racer.forward(random.randint(1, 10))
            i, j = racer.pos()
            if j >= HEIGHT // 2 - 20:
                return colors[idx]


def setup_screen(num_racers):
    screen = t.Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.title('~Death Race~')
    random.shuffle(COLORS)
    colors = COLORS[:num_racers]

    racers = create_turtle(colors)
    winner = return_winner(racers, colors)
    print("The winner of the race is", winner)
    while True:
        key = input("Press Q to exit the race: ")

        if key != 'Q':
            continue
        else:
            break


def start_game():
    num_racers = get_input()
    setup_screen(num_racers)


start_game()
