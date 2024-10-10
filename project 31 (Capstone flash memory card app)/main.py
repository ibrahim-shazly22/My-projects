from tkinter import *
import pandas
import random
import time
#-----------------------------------program sw--------------------------------------------
to_learn={}
try:
    data=pandas.read_csv("known_words.txt")
except FileNotFoundError:
    original_data=pandas.read_csv("french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")

def next_word():
    global flip_timer
    global current_card
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    random_french_word=current_card["French"]
    canvas.itemconfig(word_card,text=f"{random_french_word}",font=("arial", 60, "bold"),fill="black")
    canvas.itemconfig(title_word,text="French",font=("arial", 40, "italic"),fill="black")
    canvas.itemconfig(canvas_image, image=front_image)
    flip_timer=window.after(3000, flip_card)


def flip_card():
    current_card = random.choice(to_learn)
    random_english_word = current_card["English"]
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(word_card, text=f"{random_english_word}", font=("arial", 60, "bold"), fill="white")
    canvas.itemconfig(title_word, text="English", font=("arial", 40, "italic"), fill="white")


def known_word():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("known_words.txt", index=False)
    print(len(new_data))
    next_word()






#---------------------------------UI Interface----------------------------------------------
BACKGROUND_COLOR = "#B1DDC6"
window=Tk()
window.title("Flashy")
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,flip_card)

canvas=Canvas(width=800, height=526, highlightthickness=0)
front_image=PhotoImage(file="card_front.png")
back_image=PhotoImage(file="card_back.png")
canvas_image=canvas.create_image(400, 263, image=front_image)

title_word=canvas.create_text(400, 150, text="Title", font=("arial", 40, "italic"))
word_card=canvas.create_text(400, 263, text="Word", font=("arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)



right_image=PhotoImage(file="right.png")
right_button=Button(image=right_image,highlightthickness=0,command=known_word)
right_button.grid(column=1,row=1)

wrong_image=PhotoImage(file="wrong.png")
wrong_button=Button(image=wrong_image,highlightthickness=0,command=next_word)
wrong_button.grid(column=0,row=1)












next_word()

window.mainloop()
