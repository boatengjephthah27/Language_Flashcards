from tkinter import *
from tkinter.font import BOLD, ITALIC
import pandas as pd, random as ran, json




# ****************************************************** CONSTANTS ***********************************************************

# TODO sound to click




e_color = "#FF5B00"
o_color = "#001E6C"
bg_color = "#3399CC"
card = {}
reading_data = {}
title_text = ""
value_text = ""
# yes_count = 0
# no_count = 0






# ****************************************************** FUNCTIONS ***********************************************************







def French():
    
    yes.config(command=next_yes_word_fr)
    no.config(command=next_no_word_fr)
    
    global yes_count, no_count
    yes_count = 0
    no_count = 0
    label.itemconfig(known, text=f"known: 0{yes_count}")
    label.itemconfig(unknown, text=f"Unknown: 0{no_count}")
    
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
        
    l_change.config(
        image=fr_flag
    )
        
    next_word()
    
    popup.destroy()
    


def Spanish():
    
    yes.config(command=next_yes_word_es)
    no.config(command=next_no_word_es)

    
    global yes_count, no_count
    yes_count = 0
    no_count = 0
    label.itemconfig(known, text=f"known: 0{yes_count}")
    label.itemconfig(unknown, text=f"Unknown: 0{no_count}")
    
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
        
    l_change.config(
        image=es_flag
    )
        
    next_word()
    
    popup.destroy()


def keep_count(key_name):
     
    # opening and reading count file        
    try:
        with open("data/count_file.json","r") as file:
            data_file = json.load(file)
            try:
                file_dict = {key_name : data_file[key_name]} 
                data_file.update(file_dict)
            except KeyError:
                with open("data/count_file.json","r") as file:
                    file_dict = {key_name : 0} 
                    data_file.update(file_dict)

    except FileNotFoundError:
        with open("data/count_file.json","w") as file:
            file_dict = {key_name : 1}
            json.dump(file_dict, file, indent=1)

    else:
        if key_name in data_file:
            with open("data/count_file.json","w") as file:
                data_file[key_name] += 1
                json.dump(data_file, file, indent=1)
        # else:
        #     with open("data/count_file.json","w") as file:
        #         file_dict = {key_name : 1} 
        #         json.dump(file_dict, file)
            
            

def call_count(key_name):
    # try:
    with open("data/count_file.json","r") as file:
        data_file = json.load(file)

    # except FileNotFoundError:
    #     with open("data/count_file.json","w") as file:
    #         file_dict = {key_name : 1} 
    #         json.dump(file_dict, file)

    # else:
    if key_name in data_file:
        global no_count
        no_count = data_file[key_name]
        print(no_count)
        # else:
        #     with open("data/count_file.json","w") as file:
        #         file_dict = {key_name : 1} 
        #         json.dump(file_dict, file, indent=3)
            
        


def next_word():
    global card, flipper
    app.after_cancel(flipper)
    card = ran.choice(reading_data)
    canvas.itemconfig(title_, text=title_text, fill=o_color)
    canvas.itemconfig(word_, text=card[key_text], fill=o_color)
    canvas.itemconfig(card_img, image=img1)
    flipper = app.after(5000, func=flip)

    print(card) 
        


def next_yes_word_fr():
    
    keep_count("yes_fr")
    call_count("yes_fr")
    
    if no_count < 10:
        label.itemconfig(known, text=f"Known: 0{no_count}")
    else:
        label.itemconfig(known, text=f"Known: {no_count}")
                
    reading_data.remove(card)
    next_word()
    new_data = pd.DataFrame(reading_data)
    new_data.to_csv("data/fr_unknown_words.csv", index=False)
    
    
    
def next_yes_word_es():
    
    keep_count("yes_es")
    call_count("yes_es")
    
    if no_count < 10:
        label.itemconfig(known, text=f"Known: 0{no_count}")
    else:
        label.itemconfig(known, text=f"Known: {no_count}")
                
    reading_data.remove(card)
    next_word()
    new_data = pd.DataFrame(reading_data)
    new_data.to_csv("data/es_unknown_words.csv", index=False)
    


def next_no_word_fr():
                    
    keep_count("no_fr")
    # call_count("no_fr")
    
    global no_count
    if True:
        call_count("no_fr")
        if no_count < 10:
            label.itemconfig(unknown, text=f"Unknown: 0{no_count}")
        else:
            label.itemconfig(unknown, text=f"Unknown: {no_count}")
    
    next_word()
      
    
    
def next_no_word_es():
    
    keep_count("no_es")
    call_count("no_es")
    
    if no_count < 10:
        label.itemconfig(unknown, text=f"Unknown: 0{no_count}")
    else:
        label.itemconfig(unknown, text=f"Unknown: {no_count}")
        
    next_word()
    
    

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
    
    
    # app geometry
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    window_height = 240
    window_width = 333
    width_center = int(screen_width/2 - window_width/2)
    height_center = int(screen_height/2 - window_height/2)
    window_position = popup.geometry(f"{window_width}x{window_height}+{width_center}+{height_center}")
    popup.resizable(False,False)
    
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

# app geometry
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
window_height = 720
window_width = 693
width_center = int(screen_width/2 - window_width/2)
height_center = int(screen_height/2 - window_height/2)
window_position = app.geometry(f"{window_width}x{window_height}+{width_center}+{height_center}")
app.resizable(False,False)

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

canvas.grid(row=2, column=0, columnspan=2)

# label
label = Canvas(
    width=600,
    height=150,
    bg=bg_color,
    highlightthickness=0,    
)
label.grid(row=1, column=0, columnspan=2)

unknown = label.create_text(
    120,75,
    text="Unknown: 00",
    font=("COURIER", 32, BOLD),
)

known = label.create_text(
    480,75,
    text="Known: 00",
    font=("COURIER", 32, BOLD),
)

# buttons
no_img = PhotoImage(file="images/w.png")
no = Button (
    image=no_img,
    highlightthickness=0,
    border=0,
    command=None
)
no.grid(row=3, column=0)

yes_img = PhotoImage(file="images/r.png")
yes = Button (
    image=yes_img,
    highlightthickness=0,
    border=0,
    command=None
)
yes.grid(row=3, column=1)

# flags
l_change_img = PhotoImage(file="images/lang.png")
fr_flag = PhotoImage(file="images/frflag.png")
es_flag = PhotoImage(file="images/esflag.png")

# flag button

l_change = Button (
    image=l_change_img,
    highlightthickness=0,
    border=0,
    command=lang_choice
)
l_change.grid(row=0, column=0, columnspan=2)

lang_choice()





app.mainloop()