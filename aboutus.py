from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


class aboutus:
    def __init__(self, root):
        self.root = root
        self.root.title('HARYANA GYM')
        self.root.geometry("1100x600+100+50")

        self.bg1 = ImageTk.PhotoImage(file="gb3.jpg")
        self.bg_image1 = Label(self.root, image=self.bg1).place(x=340, y=0,relwidth=1,relheight=1.5)

        self.bg2 = ImageTk.PhotoImage(file="gb.png")
        self.bg_image2 = Label(self.root, image=self.bg2).place(x=0, y=0,relwidth=0.5,relheight=1)

        label1 = Label(root, text="ABOUT US", font=("Showcard Gothic", 20, "bold"), bg="red",fg="black")
        label1.place(x=140, y=100,relwidth=0.2,relheight=0.1)

        Frame1 = Frame(self.root, bg="white")
        Frame1.place(x=60, y=250, height=450, width=450)

        text=Label(Frame1,text="We believe that fitness should be affordable\nfor everyone and "
                               "accessible to everyone.\n At Haryana Gym, we believe that building "
                               "a\npositive culture is incredibly important.\n      we believe in "
                               "encouraging,supporting,chall\n         enging,learning "
                               "growing to be "
                               "the "
                               "best.We’\n       re committed to "
                               "training,"
                               "so you’ll be "
                               "encour\n            aged "
                               "to "
                               "improve your existing skills while\n you develop new ones. \n\n   ~Bhawna,Vaishali,Gautam",
                   font=("Showcard Gothic", 14),fg="white",bg="black")
        text.place(x=20,y=20,relwidth=0.9,relheight=0.91)
        button=Button(self.root,text="BACK",fg="black",command=self.main_window).place(x=50,y=3) 
    def main_window(self):
        self.root.destroy()
        import openingpage 

root = Tk()
obj = aboutus(root)
root.mainloop()