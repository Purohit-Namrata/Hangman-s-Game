import tkinter as tk
from tkinter import messagebox
import random

def try_again():
    global word_to_be_guessed, guesses, guessed_letters, word_label, no_of_guesses, guessed_label, guess_entry, c
    
    word_to_be_guessed = random.choice(words)
    guesses = 6
    guessed_letters = []
    
    # Clear the canvas
    c.delete("all")
    
    # Redraw the hangman structure
    c.create_line(20, 300, 120, 300)
    c.create_line(70, 300, 70, 20)
    c.create_line(70, 20, 170, 20)
    c.create_line(170, 20, 170, 50)
    
    # Update labels
    word_label.config(text=" ".join(["_" for _ in word_to_be_guessed]))
    no_of_guesses.config(text="Guesses remaining: {}".format(guesses))
    guessed_label.config(text="Guessed letters: ")
    
def check_guess():
    global guesses, guessed_letters, word_to_be_guessed, guess_entry
    
    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)
    
    if guess in guessed_letters or len(guess) != 1 or not guess.isalpha():
        return
    
    guessed_letters.append(guess)
    guessed_label.config(text="Guessed letters: {}".format(" ".join(guessed_letters)))
    
    if guess in word_to_be_guessed:
        word_display = list(word_label['text'])
        for i, letter in enumerate(word_to_be_guessed):
            if letter == guess:
                word_display[2 * i] = guess
        
        word_label.config(text="".join(word_display))
        
        if "_" not in word_display:
            messagebox.showinfo("Hangman", "You win!")
            return
    else:
        guesses -= 1
        no_of_guesses.config(text="Guesses remaining: {}".format(guesses))
        
        # Update hangman drawing
        if guesses == 5:
            c.create_oval(140, 50, 200, 110)
        elif guesses == 4:
            c.create_line(170, 110, 170, 170)
        elif guesses == 3:
            c.create_line(170, 130, 140, 140)
        elif guesses == 2:
            c.create_line(170, 130, 200, 140)
        elif guesses == 1:
            c.create_line(170, 170, 140, 190)
        elif guesses == 0:
            c.create_line(170, 170, 200, 190)
            messagebox.showinfo("Hangman", "You lose! The word was '{}'".format(word_to_be_guessed))
            return

root = tk.Tk()
root.title("Hangman Game")
root.minsize(width=600, height=600)
root.geometry("600x600")

words = ["python", "perl", "c", "cpp", "java", "html", "css", "r"]
word_to_be_guessed = random.choice(words)
guesses = 6
guessed_letters = []

c = tk.Canvas(root, width=300, height=300)
c.grid(column=0, row=0)
c.create_line(20, 300, 120, 300)
c.create_line(70, 300, 70, 20)
c.create_line(70, 20, 170, 20)
c.create_line(170, 20, 170, 50)

l1 = tk.Label(root, text="Guess the name of a programming language ")
l1.grid(row=1, column=0)

word_label = tk.Label(root, text=" ".join(["_" for _ in word_to_be_guessed]))
word_label.grid(row=2, column=0)

no_of_guesses = tk.Label(root, text="Guesses remaining: {}".format(guesses))
no_of_guesses.grid(row=3, column=0)

guessed_label = tk.Label(root, text="Guessed letters: ")
guessed_label.grid(row=4, column=0)

guess_entry = tk.Entry(root)
guess_entry.grid(row=5, column=0)

b1 = tk.Button(root, text="Check guess", command=check_guess)
b1.grid(row=6, column=0)

try_again_button = tk.Button(root, text="Try again", command=try_again)
try_again_button.grid(row=7, column=0)

exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.grid(row=8, column=0)

root.mainloop()
