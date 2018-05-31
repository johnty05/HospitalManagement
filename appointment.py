# -*- coding: utf-8 -*-
"""
Created on Thu May 31 12:35:55 2018

@author: saurav
"""
from tkinter import*
#from tkinter import Frame
#from tkinter import Label
import sqlite3

# databse connection

conn=sqlite3.connect('database.db')
print("Connected")

#Pointer to be moving around in database
#refers to cursor in database terminology

c=conn.cursor()
#the GUI window using tkinter
class Mainfile:
    def __init__(self,master):
        self.master=master
        
        #Frame creation inmaster
        self.left=Frame(master,width=800,height=720,bg='lightblue')
        self.left.pack(side=LEFT)
        self.right=Frame(master,width=800,height=720,bg='steelblue')
        self.right.pack(side=RIGHT)
        
        self.heading=Label(self.left,text="Management System Appointments",font=('arial 60 bold'),fg='black',bg='yellow')
        self.heading.place(x=0,y=0)
#Objects
root=Tk()
b=Mainfile(root)
#Dimensions of the window are being set
root.geometry("1200x720+0+0")
root.resizable(False,False)
root.mainloop()