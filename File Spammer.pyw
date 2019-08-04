from tkinter import *  
from tkinter import ttk

import os

top = Tk()  
top.title('FS3')
top.configure(background='Black')

top.geometry("200x125")  

#Label
Title = Label(top, text = "FS3", background='Black', fg="White", font=("Roboto", 16)).place(x = 73,y = 8) 
Title = Label(top, text = "FILE SPAMMER 3000", background='Black', fg="White", font=("Roboto", 9)).place(x = 35.5,y = 33)  

def spam():
    for i in range(int(e1.get()) + 1):
        Data = open(str(i) + ".txt", 'a')
        Data.write("File: " + str(i))
        e1.delete(first=0, last=22)

def delete():
    for x in range(3):
        os.system('del *.txt')

        


#Buttons
sbmitbtn = Button(top, text = "Spam",activebackground = "White", borderwidth=0, background='Black', fg="White", activeforeground = "Black",command=spam).place(x = 20, y = 100)
Deletebtn = Button(top, text = "Delete",activebackground = "White", borderwidth=0, background='Black', fg="White", activeforeground = "Black",command=delete).place(x = 130, y = 100)
Quitbtn = Button(top, text = "Quit",activebackground = "White", borderwidth=0, background='Black', fg="White", activeforeground = "Black",command=top.destroy).place(x = 80, y = 100)


#Entry
e1 = Entry(top)
e1.place(x = 35, y = 50)

top.mainloop()
