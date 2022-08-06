from tkinter import *




# ****************************************************** CONSTANTS ***********************************************************

bg_color = "#3399CC"








# ****************************************************** GUI ******************************************************************
app = Tk()
app.title("Vocabulary Flashcard")
app.config(
    padx=50,
    pady=50,
    bg=bg_color
)

canvas = Canvas(
    width=414,
    height=414,
    bg=bg_color,
    highlightthickness=0
)
img1 = PhotoImage(file="blue.png")
canvas.create_image(207,207, image=img1)

canvas.pack()



app.mainloop()