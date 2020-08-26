from tkinter import *
from tkinter import ttk
import random as r
import pyperclip

def generate_password():

    length = dropdown.get()
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if uCase.get() == 1:
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if sCase.get() == 1:
        characters.extend(list('!@#$%^&*'))
    if nCase.get() == 1:
        characters.extend(list('1234567890'))

    password = ""
    for i in range(int(length)):
        password += r.choice(characters)

    textField.delete(0, END)
    textField.insert(0, password)

def copy():
    password = textField.get()
    pyperclip.copy(password)

window = Tk()

ft = ('Verdana', 22, 'bold')

window.geometry("450x600")
window.title("Random Password Generator")

heading = Label(window, text="Random Password Generator", font=ft, fg='blue')
heading.pack(side=TOP, pady=20)

length = Label(window, text="Choose Length:", font=('Verdana', 16, 'bold'), fg='blue')
length.place(x=30, y=100)

dropdown = ttk.Combobox(window, font=('Verdana', 14))
dropdown['values'] = (8, 10, 12, 14, 16)
dropdown.place(x=200, y=100)
dropdown.current(2)

uCase = IntVar()
uppercase = Checkbutton(window, text="Include Uppercase", offvalue=0, onvalue=1, font=('Verdana', 16, 'bold'), fg='blue', variable=uCase)
uppercase.place(x=30, y=150)

sCase = IntVar()
special_character = Checkbutton(window, text="Include Special Characters", offvalue=0, onvalue=1, font=('Verdana', 16, 'bold'), fg='blue', variable=sCase)
special_character.place(x=30, y=200)

nCase = IntVar()
numbers = Checkbutton(window, text="Include Numbers", offvalue=0, onvalue=1, font=('Verdana', 16, 'bold'), fg='blue', variable=nCase)
numbers.place(x=30, y=250)

button = Button(window, text="Generate Password", height=2, font=('Verdana', 16, 'bold'), fg='red', command=generate_password)
button.place(x=30, y=300)

textField = Entry(window, font=ft)
textField.place(x=30, y=350)

copyButton = Button(window, text="Copy Password", height=2, font=('Verdana', 16, 'bold'), fg='red', command=copy)
copyButton.place(x=30, y=400)


window.mainloop()




