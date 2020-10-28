from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title('calculate your BMI')
        self.root.geometry("1100x600+100+50")
        button=Button(self.root,text="BACK",fg="black",command=self.main_window).place(x=50,y=3)
        Frame1 = Frame(self.root, bg="white")
        Frame1.place(x=600, y=280, height=500, width=500)
        label10 = Label(root, text="Don't \nWish\n for\n a\n good\n body,\n work\n for\n it", font=("Showcard Gothic", 50, "bold"), bg="BLACK", fg="#22ff19")
        label10.place(x=1260, y=20)
        label10 = Label(root, text="BMI\n tells\n you how \nBIG \nyou are.\n not how \nSICK \nyou are",
                        font=("Showcard Gothic", 50, "bold"), bg="BLACK", fg="#ff4511")
        label10.place(x=40, y=30)
        self.bg = ImageTk.PhotoImage(file="bmi.jpg")
        self.bg_image = Label(root, image=self.bg).place(x=600,y=20,width=500)
        

        self.label = Label(Frame1, text="Enter your weight in pounds",font=("Berlin Sans FB Demi", 20, "bold"), bg="white", fg="black").place(x=60,y=80)
        self.lbs = StringVar()
        Entry(Frame1, textvariable=self.lbs,font=("Goudy old style", 16, "bold"), bg="#22ff19", fg="black").place(x=130,y=130)

        self.label = Label(Frame1, text="Enter your height in feet",font=("Berlin Sans FB Demi", 20, "bold"), bg="white", fg="black").place(x=60,y=180)
        self.feet = StringVar()
        Entry(Frame1, textvariable=self.feet,font=("Goudy old style", 16, "bold"), bg="#22ff19", fg="black").place(x=130,y=230)

        self.label = Label(Frame1, text="Enter your height in inches",font=("Berlin Sans FB Demi", 20, "bold"), bg="white", fg="black").place(x=60,y=280)
        self.inches = StringVar()
        Entry(Frame1, textvariable=self.inches,font=("Goudy old style", 16, "bold"), bg="#22ff19", fg="black").place(x=130,y=330)

        # Sets a button and label to click and calculate BMI
        self.buttontext = StringVar()
        Button(Frame1, textvariable=self.buttontext, command=self.calculate,font=("Goudy old style", 15, "bold"), fg="white", bg="#334466").place(x=200,y=390)
        self.buttontext.set("Calculate")

        # Sets bmi_num to a StringVar so that when it is changed, the label will
        # update
        self.bmi_num = StringVar()
        Label(Frame1, textvariable=self.bmi_num,font=("Britannic Bold", 15, "bold"), fg="black", bg="white").place(x=160,y=430)

        # Same thing here
        self.bmi_text = StringVar()
        Label(Frame1, textvariable=self.bmi_text,font=("Britannic Bold", 15, "bold"), fg="black", bg="white").place(x=160,y=470)

        self.root.mainloop()
    def main_window(self):
        self.root.destroy()
        import openingpage    
    def calculate(self):
        # Retrieves all necessary information to calculate BMI
        weight = float(self.lbs.get())
        feet = float(self.feet.get())
        inches = float(self.inches.get())
        height = (feet*12)+inches
        bmi = float((weight*703)/(height**2))
        # Updates the status label
        self.bmi_num.set("Your BMI is %.2f" % bmi)
        if bmi < 18.5:
            self.bmi_text.set("You are underweight")
        if 18.5 <= bmi < 25:
            self.bmi_text.set("You are normal")
        if 25 <= bmi < 30:
            self.bmi_text.set("You are overweight")
        if 30<= bmi > 30:
            self.bmi_text.set("You are obese")

     

root = Tk()
root.config(bg="black")
obj = Login(root)

root.mainloop()



