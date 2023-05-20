from tkinter import *

def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1080x720")
window.configure(bg = "#fefbf6")
canvas = Canvas(
    window,
    bg = "#fefbf6",
    height = 720,
    width = 1080,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file =f"backgroundMobil.png")
background = canvas.create_image(
    541.5, 270.5,
    image=background_img)

img0 = PhotoImage(file =f"sewa1.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 118, y = 226,
    width = 101,
    height = 23)

img1 = PhotoImage(file =f"sewa2.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 309, y = 226,
    width = 92,
    height = 22)

img2 = PhotoImage(file =f"sewaMobil3.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 872, y = 438,
    width = 81,
    height = 23)

img3 = PhotoImage(file =f"sewaMobil4.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 685, y = 438,
    width = 81,
    height = 23)

img4 = PhotoImage(file =f"sewaMobil5.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 872, y = 224,
    width = 81,
    height = 23)

img5 = PhotoImage(file =f"sewaMobil6.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b5.place(
    x = 499, y = 438,
    width = 81,
    height = 23)

img6 = PhotoImage(file =f"sewaMobil7.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b6.place(
    x = 313, y = 438,
    width = 81,
    height = 23)

img7 = PhotoImage(file =f"sewaMobil8.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b7.place(
    x = 125, y = 438,
    width = 81,
    height = 23)

img8 = PhotoImage(file =f"sewamobil9.png")
b8 = Button(
    image = img8,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b8.place(
    x = 685, y = 226,
    width = 90,
    height = 23)

img9 = PhotoImage(file =f"sewaMobil10.png")
b9 = Button(
    image = img9,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b9.place(
    x = 499, y = 226,
    width = 97,
    height = 23)

window.resizable(False, False)
window.mainloop()
