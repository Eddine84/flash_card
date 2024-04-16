from tkinter import *
import random
import csv
import pandas
# CODE

current_card = {}
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    oiginal_data = pandas.read_csv("./data/french_words.csv")
    flashcard_list = oiginal_data.to_dict("records")
else:
    flashcard_list = data.to_dict("records")
    

def next_card():
            global timer ,current_card,flashcard_list
            window.after_cancel(timer)
            random_set_words = random.choice(flashcard_list)
            current_card = random_set_words
            canvas.itemconfig(card_title, text="French",fill="black")
            canvas.itemconfig(card_word, text=random_set_words["English"],fill="black")
            canvas.itemconfig(real_img,image=image)
            timer = window.after(3000, flipcard)
                
                

def flipcard():
            canvas.itemconfig(card_title, text="French" ,fill="white")
            canvas.itemconfig(card_word, text=current_card["French"],fill="white")
            canvas.itemconfig(real_img,image=back_card_image)
           
                
def remove_word():
    flashcard_list.remove(current_card)
    words_to_learn_frame = pandas.DataFrame(flashcard_list)
    words_to_learn_frame.to_csv("words_to_learn.csv", index=False)
    print(len(flashcard_list))
    next_card()


#WINDO
BACKGROUND_COLOR = "#B1DDC6"

# Créer la fenêtre principale   
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
timer = window.after(3000, flipcard)


# Créer un canevas pour afficher l'image de fond
canvas = Canvas(window, height=526, width=800 )



# Charger l'image de fond
image = PhotoImage(file="./images/card_front.png")
back_card_image = PhotoImage(file="./images/card_back.png")

# Afficher l'image sur le canevas
real_img = canvas.create_image(400, 263, image=image)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_title = canvas.create_text(400,150,text="Title", font=("Arial", 40, "italic"),fill="black")
card_word =canvas.create_text(400,263,text="word", font=("Arial", 60, "bold"),fill="black")
canvas.grid(row=0, column=0, columnspan=2)
# Lancer la boucle principale de la fenêtre
cross_image = PhotoImage(  file="./images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0,command=remove_word)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(  file="./images/right.png")
known_button = Button(image=check_image,highlightthickness=0,command=next_card)
known_button.grid(row=1, column=1)
next_card()



window.mainloop()



# kuzb ofrg jxkd juqv
