from tkinter import *


class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1080x720")
        self.configure(bg="#fefbf6")

        self.canvas = Canvas(self, bg="#fefbf6", height=720, width=1080, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        self.background_img = PhotoImage(file="background.png")
        self.background = self.canvas.create_image(540.0, 360.5, image=self.background_img)

        self.resizable(False, False)

    def btn_clicked(self):
        print("Button Clicked")

    def run(self):
        self.mainloop()




if __name__ == "__main__":
    app = App()
    app.mainloop()
