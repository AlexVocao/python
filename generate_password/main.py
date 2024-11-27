from tkinter import *
from tkinter import messagebox
from generate_password import generate_password
import pyperclip


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
        is_ok = messagebox.askokcancel(title="Confirm", message=f"website: {website}\nemail: {email}\npassword: {password}")
        print(f"is_ok={is_ok}")
        if is_ok:
            with open("data.txt", "a") as file:
                data = f"{website} | {email} | {password}\n"
                file.write(data)

            website_entry.delete(0, END)
            email_entry.delete(0, END)
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

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.insert(0, "abc@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
gen_password_btn = Button(text="Generate Password", command=gen_password)
gen_password_btn.grid(row=3, column=2)
add_btn = Button(text="Add", width=35, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
