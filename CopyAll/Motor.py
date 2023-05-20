from tkinter import *

def btn_clicked():
    print("samlekom.....")

def openWindows():
    pass

window = Tk()

window.geometry("1080x720")
window.configure(bg="#fefbf6")
canvas = Canvas(window, bg="#fefbf6", height=720, width=1080, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"backgroundMotor.png")
background = canvas.create_image(556.0, 293.5, image=background_img)

img1 = PhotoImage(file=f"sewaMotor1.png")
b1 = Button(image=img1, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")
b1.place(x=139, y=461, width=81,height=23)

img2 = PhotoImage(file=f"sewaMotor2.png")
b2 = Button(image=img2, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")
b2.place(x=323, y=249, width=92, height=22)

img3 = PhotoImage(file=f"sewaMotor3.png")
b3 = Button(image=img3, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")
b3.place(x=513, y=249, width=97, height=23)

img4 = PhotoImage(file=f"sewaMotor4.png")
b4 = Button(image=img4, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")
b4.place(x=699, y=249, width=90, height=23)

img5 = PhotoImage(file=f"sewaMotor5.png")
b5 = Button(image=img5, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")
b5.place(x=327, y=461, width=81, height=23)

img6 = PhotoImage(file=f"sewaMotor6.png")
b6 = Button(image=img6, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")
b6.place(x=513, y=461, width=81, height=23)

img7 = PhotoImage(file=f"sewaMotor7.png")
b7 = Button(image=img7, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")
b7.place(x=886, y=247, width=81, height=23)

img8 = PhotoImage(file=f"sewaMotor8.png")
b8 = Button(image=img8, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")
b8.place(x=699, y=461, width=81, height=23)

img9 = PhotoImage(file=f"sewaMotor9.png")
b9 = Button(image=img9, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")
b9.place(x=886, y=461, width=81, height=23)

img10 = PhotoImage(file=f"sewaMotor10.png")
b10 = Button(image=img10, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")
b10.place(x=132, y=249, width=101, height=23)

window.resizable(False, False)
window.mainloop()