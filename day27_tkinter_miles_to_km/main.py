from tkinter import *


def button_clicked():
    my_label["text"] = user_input.get()  # come from input


window = Tk()
window.title("My first GUI prog")
window.minsize(width=600, height=400)
window.config(padx=20, pady=20)  # create space around the window, can also be used for widget

# label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "Do not click the button"
my_label.grid(column=0, row=0)
# three-way of layout manager, pack(side=top), place(x=100, y=50) and grid(column=0 row=0)

# button
button = Button(text="click me", command=button_clicked)
button.grid(column=2, row=0)

# new_button
button = Button(text="don't click me", command=button_clicked)
button.grid(column=1, row=1)

# entry
user_input = Entry(width=10)
user_input.grid(column=3, row=2)




window.mainloop()

