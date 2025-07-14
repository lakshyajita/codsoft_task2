# Password Generator with Strength Checker

from tkinter import *
import random
import string

def generate_Password():
    num = int(entry_var.get())
    characters = ""

    if(w.get() == 1):
        characters += string.ascii_lowercase
    if(x.get() == 1):
        characters += string.ascii_uppercase
    if(y.get() == 1):
        characters += string.digits
    if(z.get() == 1):
        characters += string.punctuation

    genpassword = ""
    for i in range(num):
        a = random.choice(characters)
        genpassword += a
    password_var.set(genpassword)
    generatedPass_label.config(text=genpassword)

def pass_strength(password):
    length = len(password)
    has_lowercase = any(i.islower() for i in password) 
    has_uppercase = any(i.isupper() for i in password) 
    has_digit = any(i.isdigit() for i in password) 
    has_symbol = any(i in string.punctuation for i in password) 

    check = sum([has_lowercase, has_uppercase, has_digit, has_symbol])
    if (length >= 10 and check == 4):
        strength_label.config(text="Strong")
    elif(length >= 8 and check >= 2):
        strength_label.config(text="Moderate")
    else:
        strength_label.config(text="Weak")


window = Tk()
window.title("Password Generator")
window.geometry("550x500")

mainFrame = Frame(window,
                  bg = "#D2D7DB",
                  relief = SOLID,
                  bd = 3,
                  padx = 10,
                  pady = 10)
mainFrame.pack()

Label(mainFrame,
      text = "PASSWORD GENERATOR",
      font = ('Sans-serif', 25, 'bold'),
      bg="#D2D7DB",
      fg="#163C62",
     justify = CENTER).pack(pady = 20)

length_frame = Frame(mainFrame, bg = "#D2D7DB", padx = 10, pady = 10)
length_frame.pack()

Label(length_frame,
      text = "Password Length",
      font = ('Arial', 15, 'bold'),
      bg="#D2D7DB",
      padx = 10).pack(side = LEFT)

password_var = StringVar()
entry_var = StringVar()
Entry(length_frame,
      textvariable = entry_var,
      font = ("sunken", 10),
      width = 4,
      relief = SUNKEN,
      bd = 3).pack(side = RIGHT)

checkbox_frame = Frame(mainFrame, bg = "#D2D7DB")
checkbox_frame.pack()

w = IntVar()
checkbox1 = Checkbutton(checkbox_frame,
                        text = 'a-z',
                        variable = w,
                        onvalue = 1,
                        offvalue = 0,
                        font = ('Arial', 15),
                        bg="#D2D7DB")
checkbox1.grid(row = 0, column = 0, padx = 20, pady = 10, sticky = 'w')

x = IntVar()
checkbox2 = Checkbutton(checkbox_frame,
                        text = 'A-Z',
                        variable = x,
                        onvalue = 1,
                        offvalue = 0,
                        font = ('Arial', 15),
                        bg="#D2D7DB")
checkbox2.grid(row = 0, column = 1, padx = 20, pady = 10, sticky = 'w')

y = IntVar()
checkbox3 = Checkbutton(checkbox_frame,
                        text = '0-9',
                        variable = y,
                        onvalue = 1,
                        offvalue = 0,
                        font = ('Arial', 15),
                        bg="#D2D7DB")
checkbox3.grid(row = 1, column = 0, padx = 20, pady = 10, sticky = 'e')

z = IntVar()
checkbox3 = Checkbutton(checkbox_frame,
                        text = '!@#$%^',
                        variable = z,
                        onvalue = 1,
                        offvalue = 0,
                        font = ('Arial', 15),
                        bg="#D2D7DB")
checkbox3.grid(row = 1, column = 1, padx = 20, pady = 10, sticky = 'e')

frame3 = Frame(mainFrame, bg = "#D2D7DB")
frame3.pack(pady = 10)

generate_btn = Button(frame3,
                      text = 'Generate',
                      font = ('Arial', 15),
                      height = 1,
                      width = 10,
                      bg = 'green',
                      fg ='white',
                      relief = RAISED,
                      bd = 4,
                      command = generate_Password)
generate_btn.pack(side = LEFT, padx = 30)

quit_btn = Button(frame3,
                  text = 'Quit',
                  font = ('Arial', 15),
                  height = 1, width = 10, bg = 'red', fg = 'white',
                  relief = RAISED, bd = 4,
                  command = window.destroy)
quit_btn.pack(side = RIGHT, padx = 30)

display_label = Label(mainFrame,
                      text = 'Generated Password: ',
                      font = ('Arial', 15),
                      width = 18,
                      bg = "#D2D7DB")
display_label.pack()

generatedPass_label = Label(mainFrame,
                            text = "",
                            font=('Arial', 15, 'bold'),
                            width = 17,
                            bg = "#D2D7DB",
                            fg = "#08448d")
generatedPass_label.pack()

frame5 = Frame(mainFrame, bg = "#D2D7DB")
frame5.pack()

strength_btn = Button(frame5,
                      text = 'Password Strength?',
                      font = ('arial', 15),
                      width = 25,
                      relief = RAISED, bd = 4,
                      command = lambda:pass_strength(password_var.get())).pack(side = LEFT)

strength_label = Label(frame5,
                       text="",
                       font=('sunken', 15),
                       width = 10,
                       bg="#D2D7DB")
strength_label.pack(pady = 10, side = RIGHT)

window.mainloop()