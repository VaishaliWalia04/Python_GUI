from tkinter import *
from PIL import ImageTk

class frontpage:
    def __init__(self, root):
        self.root = root
        self.root.title('HARYANA GYM')
### MENUBAR
        menubar = Menu(root, bg="red")

        menubar.add_command(label="Home", font="arial 20 bold",command=self.home_window)
        menubar.add_command(label="About us", font="arial 20 bold",command=self.about_window)
        menubar.add_command(label="Pricing",command=self.window_price)
        menubar.add_command(label="logout",command=self.window_exit)
        
        root.config(menu=menubar)


        self.root.geometry("1100x600+100+50")

    #1 IMAGE
        self.bg = ImageTk.PhotoImage(file="g3.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0,y=0)
    #2nd image
        self.bg1 = ImageTk.PhotoImage(file="g5.jpg")
        self.bg_image1 = Label(self.root, image=self.bg1).place(x=400, y=0)
    #3rd image
        self.bg2 = ImageTk.PhotoImage(file="g6.jpg")
        self.bg_image2 = Label(self.root, image=self.bg2).place(x=800, y=0)
     #4th image
        self.bg3 = ImageTk.PhotoImage(file="g7.jpg")
        self.bg_image3 = Label(self.root, image=self.bg3).place(x=1200, y=0)
#bg images
        self.bg4 = ImageTk.PhotoImage(file="g11.jpg")
        self.bg_image4 = Label(self.root, image=self.bg4).place(x=0, y=268)

        self.bg5 = ImageTk.PhotoImage(file="g11.jpg")
        self.bg_image5 = Label(self.root, image=self.bg5).place(x=800, y=268)
#FEATURES


        label10 = Label(root, text="FEATURES THAT YOU WILL LOVE", font=("Showcard Gothic", 20, "bold"), bg="white", fg="black")
        label10.place(x=225, y=350)
        Frame1 = Frame(self.root, bg="white")
        Frame1.place(x=40, y=450, height=180, width=150)

        Frame2 = Frame(self.root, bg="white")
        Frame2.place(x=230, y=450, height=180, width=150)

        Frame3 = Frame(self.root, bg="white")
        Frame3.place(x=420, y=450, height=180, width=150)

        Frame4 = Frame(self.root, bg="white")
        Frame4.place(x=610, y=450, height=180, width=150)

        text=Label(Frame1,text="Top\nEquipment",fg="white",bg="black",font="arial 16")
        text.place(x=10,y=10,height=160,width=130)

        text = Label(Frame2, text="24/7 \navailability", fg="white", bg="black", font="arial 16")
        text.place(x=10, y=10, height=160, width=130)

        text = Label(Frame3, text="integrated\n billing", fg="white", bg="black", font="arial 16")
        text.place(x=10, y=10, height=160, width=130)

        text = Label(Frame4, text="online Web\nportal access", fg="white", bg="black", font="arial "
                                                                                          "16")
        text.place(x=10, y=10, height=160, width=130)

#try now
        button=Button(text="Calculate BMI",font=("Showcard Gothic", 20, "bold"),bg="red",fg="white",activeforeground="black",command=self.bmi_window)
        button.place(x=1000,y=400,relwidth=0.2,relheight=0.15)


#contact us

        label13 = Label(root, text="CONTACT US", font=("Showcard Gothic", 14, "bold"), bg="white", fg="black")
        label13.place(x=1180, y=560)

        label13 = Label(root, text="vbg@gmail.com", font=("Showcard Gothic", 14), bg="white", fg="black")
        label13.place(x=1250, y=620)
#INSTA
        self.bg6 = ImageTk.PhotoImage(file="i.jpg")
        self.bg_image6 = Label(self.root, image=self.bg6).place(x=1200, y=660, relwidth=0.03, relheight=0.06)

        label12 = Label(root, text="www.instagram.com", font=("Showcard Gothic", 14), bg="white", fg="black")
        label12.place(x=1250, y=670)

# FACEBOOK
        self.bg7 = ImageTk.PhotoImage(file="f3.jpg")
        self.bg_image7 = Label(self.root, image=self.bg7).place(x=1200, y=720, relwidth=0.028, relheight=0.06)

        label11 = Label(root, text="www.facebook.com", font=("Showcard Gothic", 14), bg="white", fg="black")
        label11.place(x=1250, y=725)
# EMAIL
        self.bg8 = ImageTk.PhotoImage(file="m1.jpg")
        self.bg_image8 = Label(self.root, image=self.bg8).place(x=1200, y=600, relwidth=0.03, relheight=0.06)

        label14 = Label(root, text="vbg@gmail.com", font=("Showcard Gothic", 14), bg="white", fg="black")
        label14.place(x=1250, y=620)

    def bmi_window(self):
        self.root.destroy()
        import bmi
    def home_window(self):
        self.root.destroy()
        import LOGIN 
    def about_window(self):
        self.root.destroy()
        import aboutus 
    def window_price(self):
        self.root.destroy()
        import pricingpage
    def window_exit(self):
        self.root.destroy()
        clear()                


root = Tk()
obj = frontpage(root)
root.mainloop()