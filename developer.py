from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1536x864+0+0")
        self.root.title("Face Recognition System")

        # Title label
        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(relx=0, rely=0, relwidth=1, height=45)

        # Main background image
        img_top = Image.open(r"Images\pexels-divinetechygirl-1181263__1_.jpg")
        img_top = img_top.resize((1530, 720), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        # Load and resize images for the developers
        img1 = Image.open(r"Images\dev.jpeg")
        img1 = img1.resize((200, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        img2 = Image.open(r"Images\dev.jpeg")
        img2 = img2.resize((200, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        img3 = Image.open(r"Images\dev.jpeg")
        img3 = img3.resize((200, 200), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # Placing images and labels directly on the background (no frame), adjusted for space
        img_label1 = Label(f_lbl, image=self.photoimg1, borderwidth=0)
        img_label1.place(x=1050, y=100)

        img_label2 = Label(f_lbl, image=self.photoimg2, borderwidth=0)
        img_label2.place(x=1300, y=100)  # Increased the x value for more space

        img_label3 = Label(f_lbl, image=self.photoimg3, borderwidth=0)
        img_label3.place(x=1175, y=350)  # Adjusted position to keep spacing even

        # Developer names below the images with adjusted spacing
        dev_label1 = Label(f_lbl, text="Vishakha Singh", font=("times new roman", 13, "bold"))
        dev_label1.place(x=1050, y=310)

        dev_label2 = Label(f_lbl, text="Amisha Patel", font=("times new roman", 13, "bold"))
        dev_label2.place(x=1300, y=310)  # Increased x value for space below second image

        dev_label3 = Label(f_lbl, text="Kareena", font=("times new roman", 13, "bold"))
        dev_label3.place(x=1175, y=560)  # Adjusted y value to keep space below third image


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
