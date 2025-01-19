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
#from barista_statement import barista_order_summary



window = tk.Tk ()  #TK () method to initialise a main window
window.title ("Winter cafe")  # set title
window.geometry ("500x600") #set to standard geometry 


#create widget with label title, set a welcome message and slogan for my winter cafe with font and font size
#Pack a label of the title with a couple of arguments.
title_label = ttk.Label (master = window, text = "Welcome to Winter cafe!", font = ("Times, 24 bold")) 
title_label.place (x=125, y=50)

label = ttk.Label (window, text = "Not all our drinks are cold this winter ;)", font =("times, 20"))
label.place (x=85, y = 75)



order_preference = ttk.Label (window, text = "Would you like to Eat in or Take Away?", font =("times, 20"))
order_preference.place (x=50, y = 160)

#emplty variable for list which will add orders in a dictionary format
barista_orders_list = []



#________________________________ function for eating in ________________________________

#create a function for append option for eating in the cafe
def eat_in_screen ():
        global barista_order_list
    
    
        #close the main window
        window.destroy ()
        
        #create a second window for the menu
        eat_in_window = tk.Tk ()
        eat_in_window.geometry ("500x600")
        eat_in_window.title("In Cafe Menu")

        #message to input name for the order
        order_name = tk.Label (text="please enter your name for your order:", font=("Times, 15"))
        order_name.place (x=90, y = 50)
        
        #create an entry widget for the user to enter their name in
        name_entry = ttk.Entry(eat_in_window, width=30)
        name_entry.place(x=90, y=100)
        
        #create OOP for menu items with (items: price)
        class CafeMenu:
            def __init__(self, menu):
                self.menu = {
                    "Latte": 3.0,
                    "Iced Latte": 3.5,
                    "Mocha": 3.0,
                    "Cappuchino":3.0,
                    "Tea": 2.5,
                    "Matcha":3.5,
                    "Hot Chocolate"
                    "Sandwich": 5.0,
                    "Cake": 4.0,
                    "Brownie":4.0
                } 
    
        
                
       def eat_in_menu (self):
           tk.Label (self.master, text ="Menu", font=("times, 15")).pack (side="left")
                
           self.ordering = {}
           for item, price in self.menu():
               frame - tk.frame (self.menu)
               frame.place(x=90, y=120)
               
               
        
        def confirm_order(): 
            person_name = name_entry.get()
            
            #if statement to check that the user has entered their name
            if person_name: 
                #append the name into a dictionary that corresponds with eating in
                barista_order = { "order_name" : person_name,
                                 "order type" : "Eat In" 
                                 #"drinks" : drinks_list
                                 
                                 }
                #add order to a list 
                barista_orders_list.append (barista_order)
                
            
            
            else:
                invalid_message.config(text="You must enter your name to confirm you order!")
                
            
        #create a confirm order button to confirm and append the orders to a dictionary.
        confirm_order_button = tk.Button(eat_in_window, text="confirm_order", command=confirm_order, font=("times", 12))
        confirm_order_button.place(x=200, y=350)
          
        #invalid or error message for user if the name is not entered
        invalid_message = tk.Label (text="", font=("Times, 15"), fg= "red")
        invalid_message.place (x=90, y=300)
           
        
        
        
        #initialise the eat in window 
        eat_in_window.mainloop ()
        return 
        
        
            


#________________________________ function for take out ________________________________ 

def take_out_screen():
        
        global barista_order_list
    
    
        #close the main window
        window.destroy ()
        
        #create a second window for the menu
        take_out_window = tk.Tk ()
        take_out_window.geometry ("500x600")
        take_out_window.title("Take Out Menu")

        #message to input name for the order
        order_name = tk.Label (text="please enter your name for your order:", font=("Times, 15"))
        order_name.place (x=90, y = 50)
        
        #create an entry widget for the user to enter their name in
        name_entry = ttk.Entry(take_out_window, width=30)
        name_entry.place(x=90, y=100)
        
        
        def confirm_order(): 
            person_name = name_entry.get()
            
            #if statement to check that the user has entered their name
            if person_name: 
                #append the name into a dictionary that corresponds with eating in
                barista_order = { "order_name" : person_name,
                                 "order type" : "Eat In" 
                                 #"drinks" : drinks_list
                                 
                                 }
                #add order to a list 
                barista_orders_list.append (barista_order)
            
            
            else:
                invalid_message.config(text="You must enter your name to confirm you order!")
                
            
        #create a confirm order button to confirm and append the orders to a dictionary.    
        confirm_order_button = tk.Button(take_out_window, text="confirm_order", command=confirm_order, font=("times", 12))
        confirm_order_button.place(x=200, y=350)
            
        
        #invalid or error message for user if the name is not entered
        invalid_message = tk.Label (text="", font=("Times, 15"), fg= "red")
        invalid_message.place (x=90, y=340)
                  
        
        #initialise the take out window
        take_out_window.mainloop ()
        return 


#add a button to take the user to the eat in menu
eat_in_button = tk.Button (window, text = "Eat In", width=15, height=3, font = ("Calibri, 16"), command = eat_in_screen)
#configure the button to be placed in horizontally next to the take out button
eat_in_button.place (x=50, y= 200) 

#add a button to take the user to the take out menu
take_out_button = tk.Button (window, text = "Take Out", width=15, height=3, font = ("Calibri, 16"),command = take_out_screen)
#configure the button to be placed in horizontally next to the eat in button
take_out_button.place (x=275, y=200)




        
    
    
#mainloop() to launch the window.
window.mainloop()






