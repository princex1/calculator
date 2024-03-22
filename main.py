from tkinter import *

root = Tk()
root.title("calculator")
root.geometry('290x500')

label = Label(text='calculator', font="asd 15 bold").grid(row=0, column=0)
enter = StringVar()
subtitle = Label(text="enter number:").grid(row=1, column=0)
entry = Entry(textvariable=enter).grid(row=1, column=1)


def print_ec():
    global ans
    get = enter.get()
    ans = eval(get)
    print(ans)
    ans_lab.config(text=ans)


ent_btn = Button(text="=", command=print_ec).grid(row=2, column=1)
ans_lab = Label(font="ad 11 bold")

ans_lab.grid(row=3, column=1)
mainloop()
