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


from barista_statement import barista_order_summary




window = tk.Tk ()  #TK () method to initialise a main window
window.title ("Winter cafe")  # set title
window.geometry ("400x400") #set to standard geometry 


#create widget with label title, set a welcome message and slogan for my winter cafe with font and font size
#Pack a label of the title with a couple of arguments.
title_label = ttk.Label (master = window, text = "Welcome to Winter cafe!", font = ("Times, 20 bold")) 
title_label.place (x=100, y=100)

label = ttk.Label (window, text = "Not all our coffees are cold this winter ;)", font =("times"))
label.place (x=100, y = 150)


#emplty variable for list which will add orders in a dictionary format
barista_orders_list = []


#add a button to take the user to the eat in menu
eat_in_button = tk.Button (window, text = "Eat In", command = eat_in_screen)
#configure the button to be placed in horizontally next to the take out button
eat_in_button.place (x=100, y= 200)

#add a button to take the user to the take out menu
take_out_button = tk.Button (window, text = "Take Out", command = take_out_screen)
#configure the button to be placed in horizontally next to the eat in button
take_out_button.place (x=300, y=200)

#________________________________ class testing  ________________________________


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

#create a function for append option for eating in the cafe
def eat_in_screen ():
            
        window.title("In Cafe Menu")
        label.config (text="please enter your name for your order:", font = ("Times, 15 bold"))
        person_name = tk.entry.get ()
        barista_order = { "order_name" : person_name,
                          "order type" : "eat in"
                        }  
        barista_orders_list.append (barista_order)
        
        return 



#________________________________ function for take out ________________________________ 

def take_out_screen():
        
        label.config (text="please choose your order for eating out", font = ("Times, 15 bold"))
       
        window.title("Take Out Menu")
      




def barista_window():
    
    
    return barista_order_summary


    

#ttk.button (order_summary_window, text= "confirm order", order_summary_window.destroy)

        
    
    
#mainloop() to launch the window.

window.mainloop()





