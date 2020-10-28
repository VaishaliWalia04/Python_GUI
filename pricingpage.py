from tkinter import *
from PIL import ImageTk
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title('GYM MANAGEMENT SYSTEM PRICING PAGE')
        self.root.geometry("1100x600+100+50")
        #background image
        #self.bg = ImageTk.PhotoImage(file="gym1.jpg")
        #self.bg_image = Label(self.root, image=self.bg).place(x=1,y=1)
        self.bg = ImageTk.PhotoImage(file="gyme.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=1,y=1)
        label1 = Label(root, text="STAY FIT ,LIVE LONG", font=("Showcard Gothic", 30,), fg="black")
        label1.place(x=560, y=50)
        label1 = Label(root, text="Choose Gym Packages Now At Discounted Prices ", font=("times new roman", 25,), fg="black")
        label1.place(x=470, y=120)
        #this frame is for free trial
        Frame0=Frame(self.root,bg="#ff4500")
        Frame0.place(x=250,y=200,height=80,width=990)
        label2 = Label(Frame0, text="We offer you a Free Trial,Just try it out And avail the package.", font=("Algerian", 18,"bold"),fg="black",bg="#ff4500")
        #button1=Button(self.root,text="SIGN UP",font=("Showcard Gothlic",20,"bold"),bg="#334455",fg="white")
        #button1.place(x=1030,y=207)
        label2.place(x=70,y=20)
        # this frame is for basic package
        Frame1 = Frame(self.root, bg="black",)
        Frame1.place(x=235, y=300, height=400, width=300)
        label3 = Label(Frame1, text="Basic package",font=("Algerian", 18, "bold"), fg="black",bg="#22ff11")
        label3.place(x=50, y=20)
        button2 = Button(Frame1, text="JOIN NOW",command=self.login_window, font=("Showcard Gothlic", 10, "bold"), fg="black",bg="#22ff11")
        button2.place(x=100, y=360)

        label1month = Label(Frame1, text="~ 1 Month -$100\n~ 6 Month- $1000\n~ 1 Year- $3000\n\nFacilities:\n\nAccess in Morning for 1 hour\n\n No  Trainer guidance available \n\nYoga Classes Available\n\n...more", font=("times new roman", 14,), fg="black")
        label1month.place(x=30, y=70)
        #this frame is for standard
        Frame2 = Frame(self.root, bg="black")
        Frame2.place(x=590, y=300, height=400, width=300)
        label4 = Label(Frame2, text="Standard package", font=("Algerian", 18, "bold"), fg="black",bg="#22ff11")
        label4.place(x=20, y=20)
        button3 = Button(Frame2, text="JOIN NOW", command=self.login_window,font=("Showcard Gothlic", 10, "bold"), fg="black",bg="#22ff11")
        button3.place(x=120, y=360)
        label2month = Label(Frame2, text="~ 1 Month -$500\n~ 6 Month -$1000\n~ 1 Year -$3000\n\nFacilities:\n\nAccess for 3 hours a day\n\nTrainer guidance for 1 hour\n\n Self-Defence and Yoga Classes\n\n ... more", font=("times new roman", 14,), fg="black")
        label2month.place(x=25, y=70)
        #this frame is for prime membership
        Frame3 = Frame(self.root, bg="black")
        Frame3.place(x=930, y=300, height=400, width=300)
        label5= Label(Frame3, text="Premium Package", font=("Algerian", 18, "bold"), fg="black",bg="#22ff11")
        label5.place(x=30, y=20)
        button3 = Button(Frame3, text="JOIN NOW",command=self.login_window, font=("Showcard Gothlic", 10, "bold"), fg="black",bg="#22ff11")
        button3.place(x=120, y=360)
        label3month = Label(Frame3, text="~ 1 Month -$1000\n~ 6 Month -$3000\n~ 1 Year -$6000\n\nFacilities:\n\nAccess for unlimited duration\n\nPersonal Trainer Assistance\n\n Special Exercise Theater\n\n ...more", font=("times new roman", 14,), fg="black")
        label3month.place(x=40, y=70)
        button=Button(self.root,text="BACK",fg="black",command=self.main_window).place(x=50,y=3) 
    def main_window(self):
        self.root.destroy()
        import openingpage           

    def login_window(self):
        self.root.destroy()
        import LOGIN  
           
root = Tk()
obj = Login(root)
root.mainloop()
