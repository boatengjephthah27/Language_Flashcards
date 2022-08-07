from tkinter import *
from tkinter.font import BOLD, ITALIC
import pandas as pd, random as ran, time as t




# ****************************************************** CONSTANTS ***********************************************************






e_color = "#FF5B00"
o_color = "#001E6C"
bg_color = "#3399CC"
card = {}
reading_data = {}
title_text = ""
value_text = ""







# ****************************************************** FUNCTIONS ***********************************************************


def French():
    global reading_data, title_text, key_text
    title_text = "French"
    key_text = "french"
    try:
        fr_data_unknown = pd.read_csv("data/fr_unknown_words.csv")

    except FileNotFoundError:
        fr_data = pd.read_csv("data/fr.csv")
        reading_data = fr_data.to_dict(orient="records")

    else:
        reading_data = fr_data_unknown.to_dict(orient="records")
        
    next_word()
    # fr.config(
    #     command=popup.des
    # )
    
    popup.destroy()
    


def Spanish():
    global reading_data, title_text, key_text
    title_text = "Spanish"
    key_text = "spanish"
    try:
        es_data_unknown = pd.read_csv("data/es_unknown_words.csv")

    except FileNotFoundError:
        es_data = pd.read_csv("data/es.csv")
        reading_data = es_data.to_dict(orient="records")

    else:
        reading_data = es_data_unknown.to_dict(orient="records")
        
    next_word()
    popup.destroy()


    


def next_word():
    global card, flipper
    app.after_cancel(flipper)
    card = ran.choice(reading_data)
    canvas.itemconfig(title_, text=title_text, fill=o_color)
    canvas.itemconfig(word_, text=card[key_text], fill=o_color)
    canvas.itemconfig(card_img, image=img1)
    flipper = app.after(5000, func=flip)

    print(card)
    


def next_unknown_word():
    reading_data.remove(card)
    next_word()
    new_data = pd.DataFrame(reading_data)
    new_data.to_csv("data/fr_unknown_words.csv", index=False)
    



def flip():
    canvas.itemconfig(title_, text="English", fill="yellow")
    canvas.itemconfig(word_, text=card["english"], fill="yellow")
    canvas.itemconfig(card_img, image=img2)
     



def lang_choice():
    global popup
    popup = Toplevel(app)
    popup.title('Choose Language')
    popup.config(
        padx=20,
        pady=20
    )
    
    message = "\nWhich Language \ndo you want to learn today?\n\nFrench or Spanish?\n\n\n"
    prompt = Label(
        popup,
        text=message,
        font=("COURIER", 16, BOLD)
    )
    prompt.grid(row=0, column=0, columnspan=2)
    
    # global fr
    fr = Button(
        popup,
        text='French',
        font=("COURIER", 20, "bold"),
        padx=15,
        pady=10,
        command=French
    )
    fr.grid(row=1, column=0)
    
    # global es
    es = Button(
        popup,
        text='Spanish',
        font=("COURIER", 20, "bold"),
        padx=15,
        pady=10,
        command=Spanish
    )
    es.grid(row=1, column=1)
    
    

    
    
# ****************************************************** GUI ******************************************************************






# app window
app = Tk()
app.title("Vocabulary Flashcard")
app.config(
    padx=50,
    pady=20,
    bg=bg_color
)

flipper = app.after(2000, func=flip)
app.after_cancel(flipper)

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
    text="Language",
    font=("COURIER", 30, ITALIC, BOLD),
)

word_ = canvas.create_text(
    300,250,
    text="Word",
    font=("COURIER", 45, BOLD),
    
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

l_change = Button (
    text="language",
    highlightthickness=0,
    border=0,
    command=lang_choice
)
l_change.grid(row=3, column=0, columnspan=2)

lang_choice()




app.mainloop()