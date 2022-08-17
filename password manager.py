from tkinter import *
from tkinter import messagebox
from secrets import choice
from pyperclip import copy
import json


# ---------------------------- FIND PASSWORD ----------------------------------- #
def find_password():
    website = website_entry.get()  # the website as string
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)  # read the file and save the file in a variable
    except FileNotFoundError:
        messagebox.showerror(title="Error", message=f"No details for {website} found!")
    except ValueError:
        messagebox.showerror(title="Error", message=f"Add details first!")
    else:
        if website in data:
            messagebox.showinfo(title=f"{website}", message=f"Email: {data[website]['email']}\n"
                                                            f"Password: {data[website]['password']}\n"
                                                            f"Password copied on clipboard :)")
            copy(data[website]['password'])
        else:
            messagebox.showerror(title=f"{website}", message="There is no registered username for this website!")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_entry.delete(0, END)
    all_chars = ['B', 'E', '8', 'u', 'l', '*', 'p', '@', 'g', 'k', 'A', 'N', '$', 'L', '&', 'm', 't', 'Y', 'x', 'z',
                 'X', 'H', 'S', '?', '2', 'y', '%', ':', 'D', 'j', '#', 'c', '3', '4', '7', '=', 'o', '6', '~', 'J',
                 '9', 'G', 'a', '^', '5', 'M', '1', '|', 'T', 'q', '<', 'F', 'R', 's', 'i', 'Z', 'K', 'W', 'V', 'h',
                 '/', '>', '(', 'O', 'b', 'v', '!', 'e', 'd', 'w', 'f', ')', 'r', 'P', 'n', '0', 'Q', 'C', 'U', 'I']
    password = ''.join(choice(all_chars) for _ in range(20))
    password_entry.insert(0, password)
    copy(password)  # copy the generated password on clipboard


# ---------------------------- SAVE PASSWORD ------------------------------------ #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please do not leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)  # read the file and save the file in a variable
        except ValueError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)  # write the file
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)  # write the file
        else:
            data.update(new_data)  # update the file with the new entries
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)  # write the file

        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)
        messagebox.showinfo(title="Success", message="Details successfully saved!\n"
                                                     "Password copied on clipboard :)")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# window.minsize(width=400, height=400)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)  # x and y positions
canvas.grid(column=0, row=0, columnspan=3)

# Labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, pady=5, sticky='w')
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, pady=5, sticky='w')
email_entry.insert(0, "example@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3, columnspan=2, pady=5, sticky='w')

# Buttons
add_button = Button(text="Add", width=20, command=save, highlightthickness=0)
add_button.grid(column=1, row=6, pady=2, sticky='w')

search_button = Button(text="Search", width=20, command=find_password, highlightthickness=0)
search_button.grid(column=1, row=4, pady=2, sticky='w')

generate_button = Button(text="Generate Password", width=20, command=password_generator, highlightthickness=0)
generate_button.grid(column=1, row=5, pady=2, sticky='w')

window.mainloop()


