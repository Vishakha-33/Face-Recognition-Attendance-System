import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x860+0+0")
        self.root.title("Face Recognition System")
        self.root.resizable(width=True, height=True)  # Allow window to be resizable

        # First image
        img = Image.open(r"Images\cu5.jpeg")
        img = img.resize((450, 140), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(relx=0, rely=0, relwidth=0.33, relheight=0.18)

        # Second image
        img1 = Image.open(r"Images\im.jpeg")
        img1 = img1.resize((450, 140), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(relx=0.33, rely=0, relwidth=0.33, relheight=0.18)

        # Third image
        img2 = Image.open(r"Images\ik.jpeg")
        img2 = img2.resize((500, 140), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(relx=0.66, rely=0, relwidth=0.34, relheight=0.18)

        # Background image
        img3 = Image.open(r"Images\ok.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(relx=0, rely=0.18, relwidth=1, relheight=0.82)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(relx=0, rely=0, relwidth=1, height=45)

        # # ===========time==========
        # def time():
        #     string = strftime('%H:%M:%S %p')
        #     lbl.config(text = string)
        #     lbl.after(1000,time)

        # lbl = Label(title_lbl,font=('times new roman', 14, 'bold'),background = 'white', foreground='blue')
        # lbl.place(x=0,y=0,width=110,height=50)
        # time()

        # Student button
        img4 = Image.open(r"Images\kl.jpeg")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(bg_img, image=self.photoimg4,command=self.student_details, cursor="hand2")
        b1.place(relx=0.09, rely=0.15, relwidth=0.16, relheight=0.25)
        b1_1 = Button(bg_img, text="Student Details",command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(relx=0.09, rely=0.4, relwidth=0.16, height=40)


       # Detect face button
        img5 = Image.open(r"Images\k.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b2.place(relx=0.31, rely=0.15, relwidth=0.16, relheight=0.25)

        b2_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b2_1.place(relx=0.31, rely=0.4, relwidth=0.16, height=40)

        

         # Attendance button
        img6 = Image.open(r"Images\at.jpeg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.attendance_data)
        b3.place(relx=0.53, rely=0.15, relwidth=0.16, relheight=0.25)

        b3_1 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3_1.place(relx=0.53, rely=0.4, relwidth=0.16, height=40)

        # Help button
        img7 = Image.open(r"Images\help.jpeg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.help_data)
        b4.place(relx=0.75, rely=0.15, relwidth=0.16, relheight=0.25)

        b4_1 = Button(bg_img, text="Help", cursor="hand2",command=self.help_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b4_1.place(relx=0.75, rely=0.4, relwidth=0.16, height=40)

        # Train button
        img8 = Image.open(r"Images\tr.jpeg")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b5.place(relx=0.09, rely=0.57, relwidth=0.16, relheight=0.25)

        b5_1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b5_1.place(relx=0.09, rely=0.82, relwidth=0.16, height=40)

        # Photos button
        img9 = Image.open(r"Images\ph.jpeg")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b6.place(relx=0.31, rely=0.57, relwidth=0.16, relheight=0.25)

        b6_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b6_1.place(relx=0.31, rely=0.82, relwidth=0.16, height=40)

        # Developer button
        img10 = Image.open(r"Images\dev.jpeg")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7 = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.developer_data)
        b7.place(relx=0.53, rely=0.57, relwidth=0.16, relheight=0.25)

        b7_1 = Button(bg_img, text="Developers", cursor="hand2",command=self.developer_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b7_1.place(relx=0.53, rely=0.82, relwidth=0.16, height=40)

        # Exit button
        img11 = Image.open(r"Images\exit.jpeg")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b8 = Button(bg_img, image=self.photoimg11, cursor="hand2",command=self.iExit)
        b8.place(relx=0.75, rely=0.57, relwidth=0.16, relheight=0.25)

        b8_1 = Button(bg_img, text="Exit", cursor="hand2",command=self.iExit, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b8_1.place(relx=0.75, rely=0.82, relwidth=0.16, height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", " Are you sure you want to exit the system?",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

    #--------------------------------Function buttons------------------------------
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
