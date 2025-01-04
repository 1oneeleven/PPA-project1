#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 16:48:27 2024

@author: alialshehhi
"""

#the following code is my FC723 portflio task 1


#import tkinter with an alias
import tkinter as tk
from tkinter import ttk


window = tk.Tk ()  #TK () method to initialise a main window
window.title ("Winter Kaf")  # set title
window.geometry ("414x896") #set similar dimensions/resolutions as ios apple iphone 15 pro max
"""
window.geometry ("1440x900") #set similar dimensions/resolutions as my apple macbook pro 13 inch.
"""
#craet widget with label title, set a welcome message and slogan for my winter cafe with font and font size
#Pack a label of the title with a couple of arguments.
title_label = ttk.Label (master = window, text = "Welcome to Winter Kaf!", font = ("Times, 20 bold")) 
title_label.pack() 

label = tk.Label (window, text = "Not all our coffees are cold this winter ;)", font =("times"))
label.pack()

#---------

def eat_in_screen ():
    label.config (text="please choose your order for eating in")
    window.title("In Cafe Menu")

eatin_button = tk.Button (window, text = "Eat In", command = eat_in_screen)
eatin_button.pack()

def take_out_screen():
    label.config (text="please choose your order for eating out")
    window.title("Take Out Menu")

    
takeout_button = tk.Button (window, text = "Take Out", command = take_out_screen)
takeout_button.pack()



#mainloop() to launch the window.
window.mainloop()



