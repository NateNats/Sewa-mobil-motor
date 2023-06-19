from tkinter import Tk, Canvas, Button, PhotoImage

def btn_clicked():
    print("auuu")

def back_btn():
    from Firstwindows import App
    App().mainloop()


class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1080x720")
        self.configure(bg="#fefbf6")

        self.canvas = Canvas(self, bg="#fefbf6", height=720, width=1080, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        self.load_images()
        self.create_buttons()
        background = self.canvas.create_image(541.5, 270.5, image=self.background_img)

        self.resizable(False, False)
        self.mainloop()

    def load_images(self):
        self.background_img = PhotoImage(file="backgroundMobil.png", master=self)
        self.img1 = PhotoImage(file="sewaMobil1.png", master=self)
        self.img2 = PhotoImage(file="sewaMobil2.png", master=self)
        self.img3 = PhotoImage(file="sewaMobil3.png", master=self)
        self.img4 = PhotoImage(file="sewaMobil4.png", master=self)
        self.img5 = PhotoImage(file="sewaMobil5.png", master=self)
        self.img6 = PhotoImage(file="sewaMobil6.png", master=self)
        self.img7 = PhotoImage(file="sewaMobil7.png", master=self)
        self.img8 = PhotoImage(file="sewaMobil8.png", master=self)
        self.img9 = PhotoImage(file="sewaMobil9.png", master=self)
        self.img10 = PhotoImage(file="sewaMobil10.png", master=self)


    def create_buttons(self):
        self.b1 = Button(image=self.img1, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat",
                         master=self)
        self.b1.place(x=118, y=226, width=101, height=23)

        self.b2 = Button(image=self.img2, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat",
                         master=self)
        self.b2.place(x=309, y=226, width=92, height=22)

        self.b3 = Button(image=self.img3, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat",
                         master=self)
        self.b3.place(x=872, y=438, width=81, height=23)

        self.b4 = Button(image=self.img4, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat",
                         master=self)
        self.b4.place(x=685, y=438, width=81, height=23)

        self.b5 = Button(image=self.img5, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat",
                         master=self)
        self.b5.place(x=872, y=224, width=81, height=23)

        self.b6 = Button(image=self.img6, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat",
                         master=self)
        self.b6.place(x=499, y=438, width=81, height=23)

        self.b7 = Button(image=self.img7, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat",
                         master=self)
        self.b7.place(x=313, y=438, width=81, height=23)

        self.b8 = Button(image=self.img8, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat",
                         master=self)
        self.b8.place(x=125, y=438, width=81, height=23)

        self.b9 = Button(image=self.img9, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat",
                         master=self)
        self.b9.place(x=685, y=226, width=90, height=23)

        self.b10 = Button(image=self.img10, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat",
                          master=self)
        self.b10.place(x=499, y=226, width=97, height=23)
        self.btn_close = Button(master=self, text="back", command=self.destroy)
        self.btn_close.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
