import tkinter as tk 
from tkinter import simpledialog


#FOLLOWING THE RECOMMENDED SOLUTION ##############################################################################################################################################################################################################################
recomm_word = str(input("What is your word: "))
recomm_w_length = len(recomm_word)
recomm_num_of_r_letters = tk.simpledialog.askinteger("Please answer","How many letters do you want to remove", maxvalue = (recomm_w_length - 1))

def remove_chars(word_2, number):
    print('Original string:', word_2)
    value = word_2[number:]
    return value

print("Removing characters from a string")
print(remove_chars(recomm_word, recomm_num_of_r_letters))