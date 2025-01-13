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
window.title ("Winter cafe")  # set title
window.geometry ("400x800") #set similar dimensions/resolutions as ios apple iphone 15 pro max

"""
window.geometry ("1440x900") #set similar dimensions/resolutions as my apple macbook pro 13 inch.
"""
#craet widget with label title, set a welcome message and slogan for my winter cafe with font and font size
#Pack a label of the title with a couple of arguments.
title_label = ttk.Label (master = window, text = "Welcome to Winter cafe!", font = ("Times, 20 bold")) 
title_label.pack() 

label = ttk.Label (window, text = "Not all our coffees are cold this winter ;)", font =("times"))
label.pack()

#---------

class Wintercafe:
    def dining_preference (self):
        '''
        self.window = window
        self.window.title = "Winter Cafe"
        self.button.text = "eat in"
        self.button.pack ()
        self.button.text = "take out"
        self.button.pack ()
        
    '''
        pass

def eat_in_screen ():
            
        
        label.config (text="please choose your order for eating in")
        label.place (x=50,y=200)
        window.title("In Cafe Menu")

eat_in_button = tk.Button (window, text = "Eat In", command = eat_in_screen)
eat_in_button.place (x = 200, y = 50)
eat_in_button.pack()
        


def take_out_screen():
        label.config (text="please choose your order for eating out")
        window.title("Take Out Menu")

    
take_out_button = tk.Button (window, text = "Take Out", command = take_out_screen)
take_out_button.place (x = 300 , y = 50 )
take_out_button.pack()

        

confirm_order_button = tk.button (order_summary_window, text= "confirm order", order_summary_window.destroy)


def barista_window (s):
    
    
            
    from barista_statement import barista_order_summary
        
  
        
       
        
    
    
#mainloop() to launch the window.

window.mainloop()





