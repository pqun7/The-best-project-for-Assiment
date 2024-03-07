import tkinter as tk
from tkinter import END
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter = [random.choice(letters) for char in range(nr_letters)]
    symbol = [random.choice(symbols) for char in range(nr_symbols)]
    number = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = letter + symbol + number

    random.shuffle(password_list)
    password = "".join(password_list)


    password_entry.delete(0, END)
    password_entry.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear_entry():
    wabsite_entry.delete('0', END)
    password_entry.delete('0', END)

def save():
    wabsite = wabsite_entry.get()
    password = password_entry.get()
    gmail = email_entry.get()

    new_data = {wabsite:{
        "Gmail": gmail,
        "Password": password,
    }}


    if wabsite == "" or password == "" or gmail == "":
        messagebox.showwarning("Warning", "Please add details")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading the old data
                data = json.load(data_file)

        except:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "r") as data_file:
                # Reading the old data
                data = json.load(data_file)
                # Updating old data
                data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            clear_entry()
def find_pas():
    name_wabsite = wabsite_entry.get()
    with open("data.json", "r") as data:
        try:
            data = json.load(data)
            user_data = data[name_wabsite]
            messagebox.showinfo(title=name_wabsite,
                                message=f"Gmail: {user_data['Gmail']}\nPassword: {user_data['Password']}")
        except:
            messagebox.showerror(title="error", message="Make sure the site name is correct")

def search():
        try:
           find_pas()
        except FileNotFoundError:
            with open("data.json", 'w') as json_file:
                pass
            find_pas()


#JSON
#Write: json.dump()
#Read: json.load()
#Update: json.update()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("PASSWORD GENERATOR")
window.config(padx=50, pady=50)

cnavas = tk.Canvas(width=200, height=200)
img = tk.PhotoImage(file =r"C:\Users\egtea\OneDrive\سطح المكتب\my projects\Python\100 Day\day-29\logo.png")
cnavas.create_image(100,100 , image = img)

label = tk.Label(window, image = img)
label.grid(row=0, column=1)

text_wabsite = tk.Label(text="Wabsite:", font=("Arial") )
text_wabsite.grid(row=1, column= 0)

text_email = tk.Label(text="Email/Username:", font=("Arial"))
text_email.grid(row=2, column= 0)

text_password = tk.Label(text="password:", font=("Arial"))
text_password.grid(row=3, column= 0)

wabsite_entry = tk.Entry(width=35)
wabsite_entry.grid(row=1, column= 1, columnspan=2)
wabsite_entry.focus()

email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column= 1, columnspan=2)
email_entry.insert(END, "alinazer30@gmail.com")

password_entry = tk.Entry(width=35)
password_entry.grid(row=3, column= 1)

boutton_gen = tk.Button(text="Generate Password", width=19, command=generator)
boutton_gen.grid(row=3, column=2, columnspan=4)



boutton_add = tk.Button(text="Add",width=36, command=save)
boutton_add.grid(row=4, column=1, columnspan=2)

boutton_search = tk.Button(text="Search", width=19,command=search)
boutton_search.grid(row=1, column=2, columnspan=4)




window.mainloop()