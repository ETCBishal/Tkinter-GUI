from tkinter import *

'''
author: Bishal jaiswal
date: Wednesday, February 23, 2022
purpose: For practice # from CodeWithHarry
'''

'''
pack() --> It will display the text on the window. 
Tk() --> A collection of function can be used to create an application
title --> It will set the title to the window

Note: The variable must be in proper order and pacak also must be in order

'''

window_root = Tk()

window_root.geometry("500x300")  # Determining the size of the windows
# This is the title of the window
window_root.title("**** Pycharm Welcome ****")
text_to_show = Label(text="\n\nWELCOME TO Pycharm", justify="center", font=(
    'Helvetica', 18, 'bold'))   # Writing inside the window

link_to_show = Label(
    text="\nFor more information\nLink : https://www.jetbrains.com/pycharm/")

text_to_show.pack()
link_to_show.pack()


# Locking the window. So, that user can't resize it
window_root.resizable(width=False, height=False)

window_root.mainloop()
