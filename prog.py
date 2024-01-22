import tkinter as tk 
from tkinter import simpledialog


word = str(input("What is your word: "))

word_length = len(word)

number_of_r_letter = tk.simpledialog.askinteger("Please answer","How many letters do you want to delete", maxvalue = (word_length - 1))

for letters in range(word_length):
    letters = number_of_r_letter
    print(word[letters])
    number_of_r_letter = number_of_r_letter + 1 
