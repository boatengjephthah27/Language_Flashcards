from textwrap import fill
from tkinter import *
from tkinter.font import BOLD, ITALIC
import pandas as pd, random as ran, time as t




# ****************************************************** CONSTANTS ***********************************************************






e_color = "#FF5B00"
o_color = "#001E6C"
bg_color = "#3399CC"
fr_data = pd.read_csv("data/fr.csv")
es_data = pd.read_csv("data/es.csv")
fr_dict = fr_data.to_dict(orient="records")
es_dict = es_data.to_dict(orient="records")
card = {}






# ****************************************************** FUNCTIONS ***********************************************************






def next_word():
    global card, flipper
    app.after_cancel(flip)
    card = ran.choice(fr_dict)
    canvas.itemconfig(title_, text="French", fill=o_color)
    canvas.itemconfig(word_, text=card["french"], fill=o_color)
    canvas.itemconfig(card_img, image=img1)
    flipper = app.after(5000, func=flip)

    print(card)
    


def next_unknown_word():
    fr_dict.remove(card)
    next_word()
    new_data = pd.DataFrame(fr_dict)
    new_data.to_csv("data/unknown_words.csv")
    



def flip():
    canvas.itemconfig(title_, text="English", fill="yellow")
    canvas.itemconfig(word_, text=card["english"], fill="yellow")
    canvas.itemconfig(card_img, image=img2)
     
    
    
    
    
    
    
# ****************************************************** GUI ******************************************************************






# app window
app = Tk()
app.title("Vocabulary Flashcard")
app.config(
    padx=50,
    pady=20,
    bg=bg_color
)

flipper = app.after(5000, func=flip)

# canvas
canvas = Canvas(
    width=600,
    height=414,
    bg=bg_color,
    highlightthickness=0,
)
img1 = PhotoImage(file="images/ash.png")
img2 = PhotoImage(file="images/blue.png")
card_img = canvas.create_image(300,207, image=img1)

title_ = canvas.create_text(
    300,90,
    text="",
    font=("COURIER", 30, ITALIC, BOLD),
)

word_ = canvas.create_text(
    300,250,
    text="",
    font=("COURIER", 55, BOLD),
    
)

canvas.grid(row=1, column=0, columnspan=2)

# label
label = Label(
    text="Vocabulary Flashcards",
    font=("COURIER", 30, BOLD),
    bg=bg_color,
    pady=50
)
label.grid(row=0, column=0, columnspan=2)

# buttons
no_img = PhotoImage(file="images/w.png")
no = Button (
    image=no_img,
    highlightthickness=0,
    border=0,
    command=next_word
)
no.grid(row=2, column=0)

yes_img = PhotoImage(file="images/r.png")
yes = Button (
    image=yes_img,
    highlightthickness=0,
    border=0,
    command=next_unknown_word
)
yes.grid(row=2, column=1)





next_word()


app.mainloop()