import tkinter as tk 
from tkinter import simpledialog


word = str*(input("What is your word: "))

word_length = len(word)

number_of_r_letter = tk.simpledialog.askinteger("How many letter\s do you want to delete", max = word_length - 1)

for letters in range(number_of_r_letter):
    print(word[letters > number_of_r_letter])
