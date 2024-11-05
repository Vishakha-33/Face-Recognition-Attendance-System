from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import cv2


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1536x864+0+0")
        self.root.title("Face Recognition System")

        # Title label
        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Main background image
        img_top = Image.open(r"Images\customer-service-flat-design-concept-illustration-icon-support-call-center-help-desk-hotline-operator-abstract-metaphor-can-use-for-landing-page-mobile-app-free-vector.jpg")
        img_top = img_top.resize((1530, 720), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        # Help email labels
        email_label = Label(f_lbl, text="Email:", font=("times new roman", 13, "bold"), bg="white")
        email_label.place(x=600, y=400)

        email1_label = Label(f_lbl, text="vishakhasingh@gmail.com", font=("times new roman", 13), bg="white")
        email1_label.place(x=620, y=430)  # Adjusted x position for alignment

        email2_label = Label(f_lbl, text="amishapatel@gmail.com", font=("times new roman", 13), bg="white")
        email2_label.place(x=620, y=460)  # Adjusted x position for alignment

        email3_label = Label(f_lbl, text="kareena@gmail.com", font=("times new roman", 13), bg="white")
        email3_label.place(x=620, y=490)  # Adjusted x position for alignment


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
