from tkinter import *
from tkinter import messagebox
from generate_password import generate_password
import pyperclip
import json

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    if len(website.strip()) == 0:
        messagebox.showerror(title="Error", message="Please fill the website")
    else:
        try:
            with open("data.json") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="no data file found".title())
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title=website, message=f"No details for {website} exist")





# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    password = generate_password()
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website.strip()) == 0:
        messagebox.showerror(title="Error", message="Please fill the website")
    elif len(email.strip()) == 0:
        messagebox.showerror(title="Error", message="Please fill the email")
    elif len(password.strip()) == 0:
        messagebox.showerror(title="Error", message="Please fill the password")
    else:
        new_data = {
            website: {
                "email": email,
                "password": password
            }
        }

        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)

canvas = Canvas(width=200, height=200)
canvas.grid(row=0, column=1)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)
email_entry = Entry(width=35)
email_entry.insert(0, "abc@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
gen_password_btn = Button(text="Generate Password", command=gen_password, width=21)
gen_password_btn.grid(row=3, column=2)
add_btn = Button(text="Add", width=35, command=save)
add_btn.grid(row=4, column=1, columnspan=2)
search_btn = Button(text="Search", command=find_password, width=21)
search_btn.grid(row=1, column=2)
window.mainloop()
