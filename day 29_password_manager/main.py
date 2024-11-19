from tkinter import *
from tkinter import messagebox
from password_generator import password_generator
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_p():
    generated_password = password_generator()
    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- PASSWORD RECUPERATION ------------------------------- #


def password_recuperation():
    try:
        df = open("password.json", "r")
        data = json.load(df)
        email_dict = data.get(website_entry.get(), {}).get("email")
        if email_dict is None:
            raise FileNotFoundError
        messagebox.showinfo(title=website_entry.get(),
                            message=f'email address: {data[website_entry.get()]["email"]}\n'
                                    f'password:{data.get(website_entry.get(), {}).get("password")}')
    except FileNotFoundError:
        messagebox.showinfo(title=website_entry.get(), message=f"You don't have registered an email and password "
                                                               f"for: {website_entry.get()}")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    if website_entry.get() == "" or password_entry.get() == "":
        messagebox.showinfo(title="empty entry", message="Please fill all of the entry")
    else:
        is_ok = messagebox.askokcancel(title="save confirmation",
                                       message=f'Do you wish to save for\n'
                                               f'This website: "{website_entry.get()}" \n'
                                               f'This password: "{password_entry.get()}"?')
        new_data = {
            website_entry.get(): {
                "email": email_entry.get(),
                "password": password_entry.get()
            }
        }

        if is_ok:
            try:
                # reding old data:
                df = open("password.json", "r")
                newer_data = json.load(df)
                # update data
                newer_data.update(new_data)
            except FileNotFoundError as error:
                df = open("password.json", "w")
                json.dump(new_data, df, indent=4)
            else:
                # write new data:
                df = open("password.json", "w")
                json.dump(newer_data, df, indent=4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)  # bg="#ed11d3"

# logo
canvas = Canvas(width=200, height=220, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 110, image=logo_img)
canvas.grid(column=1, row=0)

# Label
website_text = Label(text="Website:")
website_text.grid(column=0, row=1)

email_user_text = Label(text="Email/Username:")
email_user_text.grid(column=0, row=2)

password_text = Label(text="Password:")
password_text.grid(column=0, row=3)

# Button
generate_button = Button(text="Generate Password", command=generate_p)
generate_button.grid(column=2, row=3, sticky="w")

add_button = Button(text="add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

search_button = Button(text="search", width=14, command=password_recuperation)
search_button.grid(column=2, row=1, sticky="w")

# Entry
website_entry = Entry(width=32)
website_entry.grid(column=1, row=1, sticky="w")
website_entry.focus()

email_entry = Entry(width=51)
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_entry.insert(0, "usermail@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, sticky="w")

window.mainloop()
