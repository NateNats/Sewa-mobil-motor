from tkinter import Tk, Canvas, Button, PhotoImage, Text


def btn_clicked():
    print("1")

def btn_clicked2():
    print("2")

def btn_clicked3():
    print("3")

def btn_clicked4():
    print("4")

def btn_clicked5():
    print("5")

def btn_clicked6():
    print("6")

def btn_clicked7():
    print("7")

def btn_clicked8():
    print("8")

def btn_clicked9():
    print("9")

def btn_clicked10():
    print("10")

def btn_clicked11():
    print("11")

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1080x720")
        self.configure(bg="#fefbf6")
        self.canvas = Canvas(self, bg="#fefbf6", height=720, width=1080, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        self.load_images()
        self.create_buttons()
        self.create_entries()
        background = self.canvas.create_image(541.5, 270.5, image=self.background_img)

        self.resizable(False, False)
        self.mainloop()

    def load_images(self):
        self.background_img = PhotoImage(file=f"background.png", master=self)
        self.img0 = PhotoImage(file=f"img0.png", master=self)
        self.img1 = PhotoImage(file=f"img1.png", master=self)
        self.img2 = PhotoImage(file=f"img2.png", master=self)
        self.img3 = PhotoImage(file=f"img3.png", master=self)
        self.img4 = PhotoImage(file=f"img4.png", master=self)
        self.img5 = PhotoImage(file=f"img5.png", master=self)
        self.img6 = PhotoImage(file=f"img6.png", master=self)
        self.img7 = PhotoImage(file=f"img7.png", master=self)
        self.img8 = PhotoImage(file=f"img8.png", master=self)
        self.img9 = PhotoImage(file=f"img9.png", master=self)
        self.img10 = PhotoImage(file=f"img10.png", master=self)

        self.entry0_img = PhotoImage(file=f"img_textBox0.png", master=self)
        self.entry1_img = PhotoImage(file=f"img_textBox1.png", master=self)
        self.entry2_img = PhotoImage(file=f"img_textBox2.png", master=self)
        self.entry3_img = PhotoImage(file=f"img_textBox3.png", master=self)
        self.entry4_img = PhotoImage(file=f"img_textBox4.png", master=self)
        self.entry5_img = PhotoImage(file=f"img_textBox5.png", master=self)
        self.entry6_img = PhotoImage(file=f"img_textBox6.png", master=self)

    def create_buttons(self):

        b0 = Button(image=self.img0, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat", master=self)
        b0.place(x=118, y=226, width=101, height=23)


        b1 = Button(image=self.img1, borderwidth=0, highlightthickness=0, command=btn_clicked2, relief="flat", master=self)
        b1.place(x=309, y=226, width=92, height=22)


        b2 = Button(image=self.img2, borderwidth=0, highlightthickness=0, command=btn_clicked3, relief="flat", master=self)
        b2.place(x=872, y=438, width=81, height=23)


        b3 = Button(image=self.img3, borderwidth=0, highlightthickness=0, command=btn_clicked4, relief="flat", master=self)
        b3.place(x=685, y=438, width=81, height=23)


        b4 = Button(image=self.img4, borderwidth=0, highlightthickness=0, command=btn_clicked5, relief="flat", master=self)
        b4.place(x=872, y=224, width=81, height=23)



        b5 = Button(image=self.img5, borderwidth=0, highlightthickness=0, command=btn_clicked6, relief="flat", master=self)
        b5.place(x=499, y=438, width=81, height=23)

        b6 = Button(image=self.img6, borderwidth=0, highlightthickness=0, command=btn_clicked7, relief="flat", master=self)
        b6.place(x=313, y=438, width=81, height=23)

        b7 = Button(image=self.img7, borderwidth=0, highlightthickness=0, command=btn_clicked8, relief="flat", master=self)
        b7.place(x=125, y=438, width=81, height=23)

        b8 = Button(image=self.img8, borderwidth=0, highlightthickness=0, command=btn_clicked9, relief="flat", master=self)
        b8.place(x=685, y=226, width=90, height=23)

        b9 = Button(image=self.img9, borderwidth=0, highlightthickness=0, command=btn_clicked10, relief="flat", master=self)
        b9.place(x=499, y=226, width=97, height=23)

        b10 = Button(image=self.img10, borderwidth=0, highlightthickness=0, command=btn_clicked11, relief="flat", master=self)
        b10.place(x=893, y=668, width=108, height=23)


    def create_entries(self):
        self.entry0_bg = self.canvas.create_image(870.5, 605.0, image=self.entry0_img)
        entry0 = Text(bd=0, bg="#d9d9d9", highlightthickness=0, master=self)
        entry0.place(x=738, y=589, width=265, height=30)
        self.canvas.create_text(826.5, 575.5, text="Masukan Lama Peminjaman", fill="#000000", font=("None", int(12.0)))

        self.entry1_bg = self.canvas.create_image(870.5, 535.5, image=self.entry1_img)
        entry1 = Text(bd=0, bg="#d9d9d9", highlightthickness=0, master=self)
        entry1.place(x=739, y=521, width=263, height=27)
        self.canvas.create_text(826.0, 504.5, text="Masukan Tanggal Peminjaman", fill="#000000", font=("None", int(12.0)))

        self.entry2_bg = self.canvas.create_image(538.5, 606.5, image=self.entry2_img)
        entry2 = Text(bd=0, bg="#d9d9d9", highlightthickness=0, master=self)
        entry2.place(x=407, y=592, width=263, height=27)
        self.canvas.create_text(510.0, 575.5, text="Apakah Anda ingin Menambah Supir", fill="#000000", font=("None", int(12.0)))

        self.entry3_bg = self.canvas.create_image(537.5, 535.5, image=self.entry3_img)
        entry3 = Text(bd=0, bg="#d9d9d9", highlightthickness=0, master=self)
        entry3.place(x=407, y=521, width=261, height=27)
        self.canvas.create_text(494.5, 504.5, text="Masukan Syarat Peminjaman", fill="#000000", font=("None", int(12.0)))

        self.entry4_bg = self.canvas.create_image(213.5, 668.5, image=self.entry4_img)
        entry4 = Text(bd=0, bg="#d9d9d9", highlightthickness=0, master=self)
        entry4.place(x=82, y=654, width=263, height=27)
        self.canvas.create_text(161.0, 637.5, text="Masukan Alamat", fill="#000000", font=("None", int(12.0)))

        self.entry5_bg = self.canvas.create_image(212.5, 606.5, image=self.entry5_img)
        entry5 = Text(bd=0, bg="#d9d9d9", highlightthickness=0, master=self)
        entry5.place(x=82, y=592, width=261, height=27)
        self.canvas.create_text(160.0, 574.5, text="Masukan No HP", fill="#000000", font=("None", int(12.0)))

        self.entry6_bg = self.canvas.create_image(213.5, 535.5, image=self.entry6_img)
        entry6 = Text(bd=0, bg="#d9d9d9", highlightthickness=0, master=self)
        entry6.place(x=82, y=521, width=263, height=27)
        self.canvas.create_text(161.0, 504.5, text="Masukan Nama", fill="#000000", font=("None", int(12.0)))

if __name__ == "__main__":
    app = App()
    app.mainloop()
