import tkinter as tk
from tkinter import * 
from tkhtmlview import HTMLLabel
from PIL import ImageTk, Image

root = Tk()
root.geometry("700x350")
def openRec():
    rec = Toplevel(root)
    rec.title("Recordings")
    rf = LabelFrame(rec,text="Recordings")
    rf.place(relx=0.5,rely=0.5,anchor=CENTER)
    bgLabelRec = tk.Label(rec,image=background).place(x=0,y=0,relwidth=1,relheight=1)
    img =  PhotoImage(file="D:/D - Work/sid/images/goog.png") 

    button = Button(rec,text="rec").pack(padx=50, pady=50)
   #button.config(image=img)
    
def openFiles():
    file = Toplevel()
    file.title("Recordings")
    label = Label(file,text="Files").pack()
    bgLabelRem = tk.Label(file,image=background).place(x=0,y=0,relwidth=1,relheight=1)

def openSched():
    sched = Toplevel()
    sched.title("Recordings")
    label = Label(sched,text="Schedule").pack()
    bgLabelSched = tk.Label(sched,image=background).place(x=0,y=0,relwidth=1,relheight=1)

def openRem():
    rem = Toplevel()
    rem.title("Recordings")
    label = Label(rem,text="Reminders").pack()
    bgLabelRem = tk.Label(rem,image=background).place(x=0,y=0,relwidth=1,relheight=1)

background = PhotoImage(file="images/blueHex.png")

bgLabel= tk.Label(root,image=background).place(x=0,y=0,relwidth=1,relheight=1)
f = LabelFrame(root,text="Buttons",)
f.place(relx=0.5,rely=0.5,anchor=CENTER)
frbg = tk.Label(f,image=background).place(x=0,y=0,relwidth=1,relheight=1)


mybutton = Button(f, text="Recordings",command=openRec).pack(padx=50, pady=50)
mybutton2 = Button(f, text="Files",command=openFiles).pack(padx=50, pady=50)
mybutton3 = Button(f, text="Schedule",command=openSched).pack(padx=50, pady=50)
mybutton4 = Button(f, text="Reminders",command=openRem).pack(padx=50, pady=50)



root.mainloop()