from tkinter import *
from tkinter.font import BOLD, ITALIC
import pandas as pd, random as ran, time as t




# ****************************************************** CONSTANTS ***********************************************************







bg_color = "#3399CC"
fr_data = pd.read_csv("fr.csv")
es_data = pd.read_csv("es.csv")
fr_dict = fr_data.to_dict(orient="records")
es_dict = es_data.to_dict(orient="records")
card = {}






# ****************************************************** FUNCTIONS ***********************************************************






def next_word():
    global card
    card = ran.choice(fr_dict)
    canvas.itemconfig(title_, text="French")
    canvas.itemconfig(word_, text=card["french"])
    t.sleep(7)
    print(card)
    


def flip():
    canvas.itemconfig(title_, text="English")
    canvas.itemconfig(word_, text=card["english"])
    
    
    
    
    
    
# ****************************************************** GUI ******************************************************************







# app window
app = Tk()
app.title("Vocabulary Flashcard")
app.config(
    padx=50,
    pady=20,
    bg=bg_color
)

app.after(7000, func=flip)

# canvas
canvas = Canvas(
    width=600,
    height=414,
    bg=bg_color,
    highlightthickness=0,
)
img1 = PhotoImage(file="ash.png")
canvas.create_image(300,207, image=img1)

title_ = canvas.create_text(
    300,90,
    text="",
    font=("COURIER", 30, ITALIC, BOLD),
)

word_ = canvas.create_text(
    300,250,
    text="",
    font=("COURIER", 55, BOLD)
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
no_img = PhotoImage(file="w.png")
no = Button (
    image=no_img,
    highlightthickness=0,
    border=0,
    command=next_word
)
no.grid(row=2, column=0)

yes_img = PhotoImage(file="r.png")
yes = Button (
    image=yes_img,
    highlightthickness=0,
    border=0,
    command=next_word
)
yes.grid(row=2, column=1)





next_word()


app.mainloop()