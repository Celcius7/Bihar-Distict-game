import turtle
import pandas as pd
screen = turtle.Screen()
image = "bihar_img.gif"
screen.addshape(image)
screen.title("Bihar_distict_game...")
screen.setup(width=1000, height=800)
turtle.shape(image)


data = pd.read_csv("district.csv")
while(1):
    guess = screen.textinput(title="guess disticts", prompt="Guess the state :").title()
    if guess == 'Exit':
        break
    if guess in data['district'].to_list():
        district_data = data[data.district==guess]

        x = district_data.x
        y = district_data.y

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(x), int(y))
        t.write(guess)





# def get_screen_coor(x, y):
#     print(x)
#     print(y)
# turtle.onscreenclick(get_screen_coor)



# turtle.mainloop()