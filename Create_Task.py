import tkinter as tk
import random

def set_easy():
    global start_window, guess_counter
    guess_counter = 10
    start_window.destroy()
    comp_pick()

def set_medium():
    global start_window, guess_counter
    guess_counter = 5
    start_window.destroy()
    comp_pick()
    
def set_hard():
    global start_window, guess_counter
    guess_counter = 3
    start_window.destroy()
    comp_pick()
    
def set_infinite():
    global start_window, guess_counter
    guess_counter = -1
    start_window.destroy()
    comp_pick()
    
def start():
    global start_window
    #frame
    start_window = tk.Tk()
    start_window.title("Card Guessing Game")
    start_window.geometry("335x150")
    
    #label
    label1 = tk.Label(text="Welcome to my Card Guessing Game. Please select a Difficulty")
    label1.grid()
    
    #buttons
    easy_button = tk.Button(text="Easy - 10 guesses", command=set_easy)
    easy_button.grid()
    medium_button = tk.Button(text="Medium - 5 guesses", command=set_medium)
    medium_button.grid()
    hard_button = tk.Button(text="Hard - 3 guesses", command=set_hard)
    hard_button.grid()
    infinite_button = tk.Button(text="Infinite guesses", command=set_infinite)
    infinite_button.grid()
    
    start_window.mainloop()

def guess_counter_disp():
    global guess_counter
    if guess_counter < 0:
        return "infinite"
    else:
        return guess_counter

def set_spades():
    global guess_suit
    guess_suit = "spades"
    
def set_hearts():
    global guess_suit
    guess_suit = "hearts"

def set_clubs():
    global guess_suit
    guess_suit = "clubs"
    
def set_diamonds():
    global guess_suit
    guess_suit = "diamonds"
    
def check():
    global guess_suit, guess_value, comp_suit, comp_value, guess_counter
    
    guess_value = str(enter_value.get()).lower()
    
    #make guess_value able to be compared to comp_value
    if guess_value == "a" or guess_value == "ace":
        guess_value = 1
    elif guess_value == "j" or guess_value == "jack":
        guess_value = 11
    elif guess_value == "q" or guess_value == "queen":
        guess_value = 12
    elif guess_value == "k" or guess_value == "king":
        guess_value = 13
    else:
        guess_value = int(guess_value)
        
    #compare guess_value to comp_value
    if guess_value < comp_value:
        value_output = "too low"
    elif guess_value > comp_value:
        value_output = "too high"
    else:
        value_output = "correct"
    
    #compare guess_suit to comp_suit
    if guess_suit != comp_suit:
        suit_output = "wrong suit"
    else:
        suit_output = "right suit"
    
    #determine what to do based on the guesses
    if value_output == "correct" and suit_output == "right suit":
        guess_window.destroy()
        end("win")
    else:
        guess_counter -= 1
        if guess_counter == 0:
            guess_window.destroy()
            end("lose")
        else:
            #string of all the info being put into the output_text down below
            output = """You guessed: """ + str(enter_value.get()).lower() + """ of """ + guess_suit + """
Value: """ + value_output + """
Suit: """ + suit_output + """
Guesses remaining: """ + str(guess_counter)
            
            #update output window
            output_text = tk.Text(master=guess_window, height=5, width=35)
            output_text.grid(column=0, row=7)
            output_text.insert(tk.END, output)
       
def end(condition):
    global comp_value, comp_suit, end_window
    
    if comp_value == 1:
        comp_value = "ace"
    elif comp_value == 11:
        comp_value = "jack"
    elif comp_value == 12:
        comp_value = "queen"
    elif comp_value == 13:
        comp_value = "king"
    else:
        comp_value = str(comp_value)
        
    if condition == "win":
        title = "You Win!"
        message = "Congratulations! You guessed the " + comp_value + " of " + comp_suit + "!"
    else:
        title = "You lose."
        message = "Unfortunately, you did not guess the " + comp_value + " of " + comp_suit + " before your number of guesses reached 0."
        
    end_window = tk.Tk()
    end_window.title(title)
    
    label3 = tk.Label(text=message)
    label3.grid()
    
    restart_button = tk.Button(text="Try again", command=restart)
    restart_button.grid(row=2, column=0)
    
    end_window.mainloop()    

def restart():
    global end_window
    end_window.destroy()
    start()

def comp_pick():
    global comp_suit, comp_value
    #Suits and Values from which the computer can choose
    suit_list = ["spades", "hearts", "clubs", "diamonds"]
    value_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    #Computer chooses a Suit and a Value from the lists above
    comp_suit = random.choice(suit_list)
    comp_value = random.choice(value_list)
    
    #begin guessing
    guessing()

def guessing():
    global guess_window, guess_counter, comp_suit, comp_value, enter_value
    
    #frame
    guess_window = tk.Tk()
    guess_window.title("Card Guessing Game")
    guess_window.geometry("370x250")
    
    #label
    label2 = tk.Label(text="A Computer has chosen a card at random.")
    label2.grid()
    
    #suit buttons
    spades_button = tk.Button(text="Spades", command=set_spades)
    spades_button.grid(row=2, column=0)
    hearts_button = tk.Button(text="Hearts", command=set_hearts)
    hearts_button.grid(row=3, column=0)
    clubs_button = tk.Button(text="Clubs", command=set_clubs)
    clubs_button.grid(row=4, column=0)
    diamonds_button = tk.Button(text="Diamonds", command=set_diamonds)
    diamonds_button.grid(row=5, column=0)
    
    #enter value
    enter_value = tk.Entry(width=50)
    enter_value.grid(row=6, column=0)
    
    #entry button
    entry_button = tk.Button(text="Enter", command=check)
    entry_button.grid(row=6, column=1)
    
    guess_window.mainloop()
    
start()