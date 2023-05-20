from tkinter import *


def btn_Motor():
    # error cuy
    import Motor
    Motor.openWindows()

def btn_Mobil():
    # error cuy
    import Mobil
    Mobil.openWindows()

window = Tk()

window.geometry("1080x720")
window.configure(bg="#fefbf6")
canvas = Canvas(window, bg="#fefbf6", height=720, width=1080, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

img0 = PhotoImage(file=f"motorButton.png")
b0 = Button(image=img0, borderwidth=0, highlightthickness=0, command=btn_Motor, relief="flat")
b0.place(x=80, y=552, width=398, height=102)

img1 = PhotoImage(file =f"MobilButton.png")
b1 = Button(image=img1, borderwidth=0, highlightthickness=0, command=btn_Mobil, relief="flat")
b1.place(x=600, y=552, width=398, height=102)

background_img = PhotoImage(file=f"backgroundMenu.png")
background = canvas.create_image(546, 320, image=background_img)

window.resizable(False, False)
window.mainloop()