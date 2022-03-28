from cgitb import text
from tkinter import *

root = Tk()
root.title("Validação")
root.geometry("400x400")

def number():
    try:
        float(my_box.get())
        answer.config(text="Parabén é um fload")
    except ValueError:
        answer.config(text="That is NOT a number! Congrats!")

my_label = Label(root, text="Enter a Number")
my_label.pack(pady=20)

my_box = Entry(root)
my_box.pack(pady=10)

my_button = Button(root, text="Enter a Number",command=number)
my_button.pack(pady=5)

answer = Label(root, text='')
answer.pack(pady=20)


root.mainloop()