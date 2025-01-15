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
window.geometry ("400x400") #set to standard geometry 


#create widget with label title, set a welcome message and slogan for my winter cafe with font and font size
#Pack a label of the title with a couple of arguments.
title_label = ttk.Label (master = window, text = "Welcome to Winter cafe!", font = ("Times, 20 bold")) 
title_label.grid(row=0,column=2, pady=10)

label = ttk.Label (window, text = "Not all our coffees are cold this winter ;)", font =("times"))
label.grid(row=1,column=2, pady=10)

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
    
#________________________________ function for eating in ________________________________

def eat_in_screen ():
            
        
        label.config (text="please choose your order for eating in", font = ("Times, 15 bold"))
      
        window.title("In Cafe Menu")
        

eat_in_button = tk.Button (window, text = "Eat In", command = eat_in_screen)
eat_in_button.grid(row=2,column=1, padx=10, pady=40)

#________________________________ function for take out ________________________________ 

def take_out_screen():
        
        label.config (text="please choose your order for eating out", font = ("Times, 15 bold"))
       
        window.title("Take Out Menu")
      

    
take_out_button = tk.Button (window, text = "Take Out", command = take_out_screen)
take_out_button.grid(row=2,column=3, padx=20, pady=40)


def review_order_screen():
    
    pass

    

#ttk.button (order_summary_window, text= "confirm order", order_summary_window.destroy)

"""
def barista_window (s):
    
        
            
    from barista_statement import barista_order_summary
        
  
        
       """
        
    
    
#mainloop() to launch the window.

window.mainloop()





