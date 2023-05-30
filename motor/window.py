from tkinter import *

def btn_clicked():
    print("Button Clicked")


window = Tk()

window.title("Daftar Motor")
window.geometry("1080x720")
window.configure(bg="#fefbf6")
canvas = Canvas(window, bg="#fefbf6",height=720, width=1080, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(556.0, 293.5, image=background_img)

img0 = PhotoImage(file=f"img0.png")
b0 = Button(image=img0, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")
b0.place(x=139, y=461,width=81,height=23)

img1 = PhotoImage(file=f"img1.png")
b1 = Button(image=img1,borderwidth=0,highlightthickness=0,command=btn_clicked,relief="flat")
b1.place(x=323, y=249,width=92,height=22)

img2 = PhotoImage(file=f"img2.png")
b2 = Button(image=img2,borderwidth=0,highlightthickness=0,command=btn_clicked,relief="flat")
b2.place(x=513, y=249, width=97, height=23)

img3 = PhotoImage(file=f"img3.png")
b3 = Button(image=img3, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")
b3.place(x=699, y=249, width=90, height=23)

img4 = PhotoImage(file=f"img4.png")
b4 = Button(image=img4, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")
b4.place(x=327, y=461, width=81, height=23)

img5 = PhotoImage(file=f"img5.png")
b5 = Button(image=img5, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")
b5.place(x=513, y=461, width=81, height=23)

img6 = PhotoImage(file=f"img6.png")
b6 = Button(image=img6, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")
b6.place(x=886, y=247, width=81, height=23)

img7 = PhotoImage(file=f"img7.png")
b7 = Button(image=img7, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")
b7.place(x=699, y=461, width=81, height=23)

img8 = PhotoImage(file=f"img8.png")
b8 = Button(image=img8, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")
b8.place(x=886, y=461, width=81, height=23)

img9 = PhotoImage(file=f"img9.png")
b9 = Button(image=img9, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")
b9.place(x=132, y=249, width=101, height=23)

img10 = PhotoImage(file=f"img10.png")
b10 = Button(image=img10, borderwidth=0, highlightthickness=0, command=btn_clicked, relief="flat")
b10.place(x=841, y=663, width=108, height=23)

entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(893.5, 637.0, image=entry0_img)
entry0 = Entry(bd=0, bg="#d9d9d9", highlightthickness=0)
entry0.place(x=761, y=621, width=265, height=30)
canvas.create_text(849.5, 602.5, text="Masukan Lama Peminjaman", fill="#000000", font=("None", int(12.0)))

entry1_img = PhotoImage(file=f"img_textBox1.png")
entry1_bg = canvas.create_image(893.5, 560.0, image=entry1_img)
entry1 = Entry(bd=0, bg="#d9d9d9", highlightthickness=0)
entry1.place(x=761, y=544, width=265, height=30)
canvas.create_text(850.5, 525.5, text="Masukan Tanggal Peminjaman", fill="#000000", font=("None", int(12.0)))

entry2_img = PhotoImage(file=f"img_textBox2.png")
entry2_bg = canvas.create_image(561.5, 637.0, image=entry2_img)
entry2 = Entry(bd=0, bg="#d9d9d9", highlightthickness=0)
entry2.place(x=430, y=621, width=263, height=30)
canvas.create_text(520.0, 602.5, text="Masukan Syarat Peminjaman", fill="#000000", font=("None", int(12.0)))

entry3_img = PhotoImage(file=f"img_textBox3.png")
entry3_bg = canvas.create_image(560.5, 560.0, image=entry3_img)
entry3 = Entry(bd=0, bg="#d9d9d9", highlightthickness=0)
entry3.place(x=428, y=544, width=265, height=30)
canvas.create_text(507.5, 525.5, text="Masukan Alamat", fill="#000000", font=("None", int(12.0)))

entry4_img = PhotoImage(file=f"img_textBox4.png")
entry4_bg = canvas.create_image(228.5, 637.0, image=entry4_img)
entry4 = Entry(bd=0, bg="#d9d9d9", highlightthickness=0)
entry4.place(x=97, y=621, width=263, height=30)
canvas.create_text(176.5, 602.5, text="Masukan No HP", fill="#000000", font=("None", int(12.0)))

entry5_img = PhotoImage(file=f"img_textBox5.png")
entry5_bg = canvas.create_image(227.5, 560.0, image=entry5_img)
entry5 = Entry(bd=0, bg="#d9d9d9", highlightthickness=0)
entry5.place(x=95, y=544, width=265, height=30)
canvas.create_text(174.5, 525.5, text="Masukan Nama", fill="#000000", font=("None", int(12.0)))

window.resizable(False, False)
window.mainloop()
