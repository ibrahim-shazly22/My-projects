from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website_entry.grid(column=1,row=1,columnspan=2)

email_username_label=Label(text="Email/Username:")
email_username_label.grid(column=0,row=2)
email_entry=Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2)

password_label=Label(text="Password:")
password_label.grid(column=0,row=3)
password_entry=Entry(width=21)
password_entry.grid(column=1,row=3)

generate_button=Button(text="Generate Password")
generate_button.grid(column=2,row=3)

add_button=Button(text="Add",width=36)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()