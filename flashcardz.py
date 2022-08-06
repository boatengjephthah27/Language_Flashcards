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
    width=400,
    height=400
)
img1 = PhotoImage(file="blue.png")
canvas.create_image(200,200, image=img1)

canvas.pack()



app.mainloop()