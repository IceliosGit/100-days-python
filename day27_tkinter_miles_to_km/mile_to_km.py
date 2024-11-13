from tkinter import *

window = Tk()
window.title("miles to km converter")
window.minsize(width=300, height=50)


def button_clicked():
    km_converted["text"] = round(int(user_input.get())*1.609)


# button
button = Button(text="convert", command=button_clicked)
button.grid(column=1, row=2)

# input
user_input = Entry(width=10)
user_input.grid(column=1, row=0)

# label
miles = Label(text="Miles")
miles.grid(column=2, row=0)

km = Label(text="Km")
km.grid(column=2, row=1)

is_egal = Label(text="is egal to")
is_egal.grid(column=0, row=1)

km_converted = Label(text=0)
km_converted.grid(column=1, row=1)


window.mainloop()
