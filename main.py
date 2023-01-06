import turtle
import pandas

screen = turtle.Screen()
screen.title("Slovak okres hra")
image = "blank_okres_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("8_okres.csv")
cele_okresy = data.okres.to_list()
guessed_okres = []

while len(guessed_okres) < 8:
    answer_okres = screen.textinput(title=f"{len(guessed_okres)}/8 Okres correct", prompt="Name another okres.").title()

    if answer_okres == "Exit":
        missing_okres = []
        for okres in cele_okresy:
            if okres not in guessed_okres:
                missing_okres.append(okres)
        new_data = pandas.DataFrame(missing_okres)
        new_data.to_csv("okres_to_learn.csv")
        break
    if answer_okres in cele_okresy:
        guessed_okres.append(answer_okres)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        okres_data = data[data.okres == answer_okres]
        t.goto(int(okres_data.x), int(okres_data.y))
        t.write(answer_okres)

screen.exitonclick()