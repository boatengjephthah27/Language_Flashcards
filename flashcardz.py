from tkinter import *
from tkinter.font import BOLD, ITALIC




# ****************************************************** CONSTANTS ***********************************************************

bg_color = "#3399CC"








# ****************************************************** GUI ******************************************************************

# app window
app = Tk()
app.title("Vocabulary Flashcard")
app.config(
    padx=50,
    pady=20,
    bg=bg_color
)

# canvas
canvas = Canvas(
    width=600,
    height=414,
    bg=bg_color,
    highlightthickness=0,
)
img1 = PhotoImage(file="ash.png")
canvas.create_image(300,207, image=img1)

canvas.create_text(
    300,90,
    text="Title",
    font=("COURIER", 30, ITALIC, BOLD),
)

canvas.create_text(
    300,250,
    text="Word",
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
    padx=20
)
no.grid(row=2, column=0)

yes_img = PhotoImage(file="r.png")
yes = Button (
    image=yes_img,
    highlightthickness=0,
    border=0,
    padx=20
)
yes.grid(row=2, column=1)







app.mainloop()