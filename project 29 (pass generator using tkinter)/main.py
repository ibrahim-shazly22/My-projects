from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list=[random.choice(letters)for _ in range(nr_letters)]
    sym_list=[ random.choice(symbols)for _ in range(nr_symbols)]
    num_list=[random.choice(numbers)for _ in range(nr_numbers)]
    password_list=letter_list+sym_list+num_list
    random.shuffle(password_list)
    my_pass="".join(password_list)
    print(f"Your password is: {my_pass}")
    password_entry.insert(0,my_pass)
    pyperclip.copy(my_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    Email=email_entry.get()
    Password=password_entry.get()
    Website=website_entry.get()
    new_data={
        Website:{"Email":Email,
                 "Password":Password
                       }
    }

    if len(email_entry.get())==0 or len(password_entry.get())==0:
        messagebox.askretrycancel(title="Error",message="please do not leave empty fields")
    else:
        try:
            f=open("data.json","r")
            data = json.load(f)
        except FileNotFoundError:
            f=open("data.json","w")
            json.dump(new_data,f,indent=4)
        else:
            #replace the old data with updated data
            data.update(new_data)
            #saving the updated data
            with open("data.json", mode="w") as f:
                json.dump(data,f,indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

def search():
    website=website_entry.get()
    try:
        with open ("data.json") as file:
            data=json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="this web is not found")
    else:    
        if website in data:
            user_email_req=data[website]["Email"]
            web_pass=data[website]["Password"]
            messagebox.showinfo(title=f"{website}", message=f"email:{user_email_req}\npassword:{web_pass}")


# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title("Password Manger")
window.config(padx=20,pady=20)



canvas=Canvas(width=200,height=200)
my_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=my_image)
canvas.grid(column=1,row=0)

website_label=Label(text="Website:")
website_label.grid(column=0,row=1,)
website_entry=Entry(width=35)
website_entry.focus()
website_entry.grid(column=1,row=1,columnspan=2)

email_username_label=Label(text="Email/Username:")
email_username_label.grid(column=0,row=2)
email_entry=Entry(width=35)
email_entry.insert(0,"hemasamir770@gmail.com")
email_entry.grid(column=1,row=2,columnspan=2)

password_label=Label(text="Password:")
password_label.grid(column=0,row=3)
password_entry=Entry(width=35)
password_entry.grid(column=1,row=3)

generate_button=Button(text="Generate Password",width=15,command=generate_pass)
generate_button.grid(column=3,row=3)

add_button=Button(text="Add",width=30,command=save_data)
add_button.grid(column=1,row=4,columnspan=2)

search_button=Button(text="search",width=15,command=search)
search_button.grid(column=3,row=1)













window.mainloop()
