# -*- coding: utf-8 -*-
"""
Created on Thu May 31 12:35:55 2018

@author: saurav
"""
from tkinter import*
import tkinter.messagebox as tkm
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
        self.left=Frame(master,width=800,height=720,bg='black')
        self.left.pack(side=LEFT)
        self.right=Frame(master,width=800,height=720,bg='steelblue')
        self.right.pack(side=RIGHT)
        
        self.heading=Label(self.left,text="Doctor Management",font=('arial 60 bold'),fg='white',bg='black')
        self.heading.place(x=0,y=0)
        
        ##name of patient
        self.name=Label(self.left,text="Patient Name",font=('arial 18 bold'),fg='white',bg='black')
        self.name.place(x=50,y=200)
        #age of patient
        self.age=Label(self.left,text="Age",font=('arial 18 bold'),fg='white',bg='black')
        self.age.place(x=50,y=250)
        #gender of patient
        self.gender=Label(self.left,text="Gender",font=('arial 18 bold'),fg='white',bg='black')
        self.gender.place(x=50,y=300)
        #address
        self.location=Label(self.left,text="Location",font=('arial 18 bold'),fg='white',bg='black')
        self.location.place(x=50,y=350)
        #appointment
        self.time=Label(self.left,text="Time",font=('arial 18 bold'),fg='white',bg='black')
        self.time.place(x=50,y=400)
        #phone
        self.phone=Label(self.left,text="Phone",font=('arial 18 bold'),fg='white',bg='black')
        self.phone.place(x=50,y=450)
        
        #Since we have created the labels for all the info
        #Now we need to create lables to accept entries
        
        self.nameEntry=Entry(self.left,width=50)
        self.nameEntry.place(x=250,y=210)
        self.ageEntry=Entry(self.left,width=10)
        self.ageEntry.place(x=250,y=260)
        self.genderEntry=Entry(self.left,width=20)
        self.genderEntry.place(x=250,y=310)
        self.locEntry=Entry(self.left,width=50)
        self.locEntry.place(x=250,y=360)
        self.timeEntry=Entry(self.left,width=20)
        self.timeEntry.place(x=250,y=410)
        self.phoneEntry=Entry(self.left,width=20)
        self.phoneEntry.place(x=250,y=460)
        
        #creating a button
        self.done=Button(self.left,text='Fix Appointment',width=20,height=3,bg='white',command=self.addAppointment)
        self.done.place(x=310,y=560)
    
    def addAppointment(self):
        #print("AllSet this was for checking")
        #get() for user inputs
        #somewhat similar to C++/object oriented programming
        self.x1=self.nameEntry.get()
        self.x2=self.ageEntry.get()
        self.x3=self.genderEntry.get()
        self.x4=self.locEntry.get()
        self.x5=self.timeEntry.get()
        self.x6=self.phoneEntry.get()
        
        #To check if the above thoings are working or not....
        #Dummy Print
        #print(self.x1)
        #print(self.x2)
        #print(self.x3)
        #print(self.x4)
        #print(self.x5)
        #print(self.x6)
        if self.x1=='' or self.x2=='' or self.x3=='' or self.x4=='' or self.x5=='' or self.x6=='' :
            #print("All boxes are cumpolsury")
            tkm.showinfo("ERROR!!!","All boxes are cumpulsory")
        else:
            print("ALL INPUTS Done")
            #database transfer of details
            sql= "insert into 'appointments' (name,age,gender,location,scheduled_time,phone) values(?,?,?,?,?,?)"
            c.execute(sql,(self.x1,self.x2,self.x3,self.x4,self.x5,self.x6))
            conn.commit()
            print("database retrieval successful!!!")
#Objects
root=Tk()
b=Mainfile(root)
#Dimensions of the window are being set
#root.geometry('%dx%d+%d+%d' % (width, height, x, y))----got to know from StackOverflow
root.geometry("1200x720+0+0")
root.resizable(False,False)
root.mainloop()