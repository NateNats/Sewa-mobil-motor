from tkinter import Tk, Canvas, Button, PhotoImage

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1080x720")
        self.configure(bg="#fefbf6")

        self.canvas = Canvas(self, bg="#fefbf6", height=720, width=1080, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        self.load_images()
        self.create_buttons()

        self.resizable(False, False)
        self.mainloop()

    def load_images(self):
        self.background_img = PhotoImage(file="backgroundMotor.png", master=self)
        self.img1 = PhotoImage(file="sewaMotor1.png", master=self)
        self.img2 = PhotoImage(file="sewaMotor2.png", master=self)
        self.img3 = PhotoImage(file="sewaMotor3.png", master=self)
        self.img4 = PhotoImage(file="sewaMotor4.png", master=self)
        self.img5 = PhotoImage(file="sewaMotor5.png", master=self)
        self.img6 = PhotoImage(file="sewaMotor6.png", master=self)
        self.img7 = PhotoImage(file="sewaMotor7.png", master=self)
        self.img8 = PhotoImage(file="sewaMotor8.png", master=self)
        self.img9 = PhotoImage(file="sewaMotor9.png", master=self)
        self.img10 = PhotoImage(file="sewaMotor10.png", master=self)

    def create_buttons(self):
        b1 = Button(image=self.img1, borderwidth=0, highlightthickness=0, command=self.btn_clicked, relief="flat", master=self)
        b1.place(x=139, y=461, width=81, height=23)

        b2 = Button(image=self.img2, borderwidth=0, highlightthickness=0, command=self.btn_clicked, relief="flat", master=self)
        b2.place(x=323, y=249, width=92, height=22)

        b3 = Button(image=self.img3, borderwidth=0, highlightthickness=0, command=self.btn_clicked, relief="flat", master=self)
        b3.place(x=513, y=249, width=97, height=23)

        b4 = Button(image=self.img4, borderwidth=0, highlightthickness=0, command=self.btn_clicked, relief="flat", master=self)
        b4.place(x=699, y=249, width=90, height=23)

        b5 = Button(image=self.img5, borderwidth=0, highlightthickness=0, command=self.btn_clicked, relief="flat", master=self)
        b5.place(x=327, y=461, width=81, height=23)

        b6 = Button(image=self.img6, borderwidth=0, highlightthickness=0, command=self.btn_clicked, relief="flat", master=self)
        b6.place(x=513, y=461, width=81, height=23)

        b7 = Button(image=self.img7, borderwidth=0, highlightthickness=0, command=self.btn_clicked, relief="flat", master=self)
        b7.place(x=886, y=247, width=81, height=23)

        b8 = Button(image=self.img8, borderwidth=0, highlightthickness=0, command=self.btn_clicked, relief="flat", master=self)
        b8.place(x=699, y=461, width=81, height=23)

        b9 = Button(image=self.img9, borderwidth=0, highlightthickness=0, command=self.btn_clicked, relief="flat", master=self)
        b9.place(x=886, y=461, width=81, height=23)

        b10 = Button(image=self.img10, borderwidth=0, highlightthickness=0, command=self.btn_clicked, relief="flat", master=self)
        b10.place(x=132, y=249, width=101, height=23)
        self.btn_close = Button(master=self, text="back", command=self.destroy)
        self.btn_close.pack()

        background = self.canvas.create_image(556.0, 293.5, image=self.background_img)

    def btn_clicked(self):
        # Handle button click event
        print("samlekom.....")



if __name__ == "__main__":
    app = App()
    app.mainloop()
