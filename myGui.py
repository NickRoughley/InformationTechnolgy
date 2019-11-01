from guizero import App, Text, TextBox, PushButton, Picture

app = App(title="Nicholas Roughley", bg='blue', width=1920, height=1080)

username = "Nicky"
password = "password"

def check_input():
    if un_box.value == username and pw_box.value == password:
        #message = Text(app, text='Correct')
        Picture(app, image="Tick.png")
    else:
        #message = Text(app, text="Incorrect!")
        Picture(app, image="giphy.gif")
        app.warn(title='Warning Virus Detected', text="Virus Detected")

text1 = Text(app, text="Username", size=30, font="Algerian", color='white', align="top")
un_box = TextBox(app, width=20, height=20)
text2 = Text(app, text="Password", size=30, font="Algerian", color='white', align="top")
pw_box = TextBox(app, width=20, height=20)
submit = PushButton(app, text="submit", command=check_input)

# app.yesno(title="Yes or No", text = "Would you like to close this window?")

app.display()

