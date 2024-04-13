import customtkinter
from tkinter import PhotoImage
from keyboardList import keyboardMac

width = 1280
height = 720
nameOfApp = "Keybi"
iconPath = "src/content/keyboard.png"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title(nameOfApp)
        self.geometry(f"{width}x{height}")
        self.resizable(width=False, height=False)
        icon = PhotoImage(file=iconPath)
        self.iconphoto(True, icon)
        self.canvas = customtkinter.CTkCanvas(
            self,
            width=width,
            height=height - 40,
            bg="#242424",
            highlightbackground="black"
        )
        self.canvas.place(x=-3, y=40)

    def keyDisplay(self, __x0: int, __y0: int, __x1: int, __y1: int, sign: str) -> None:
        self.canvas.create_rectangle(__x0, __y0, __x1, __y1, fill="#242424")
        self.canvas.create_text(__x0+15, __y0+15, text=sign)

    def keyDisplay1(self, __x0: int, __y0: int, __x1: int, __y1: int) -> None:
        self.canvas.create_rectangle(__x0, __y0, __x1, __y1, fill="#FF1493")


app = App()

for i in keyboardMac.values():
    app.keyDisplay(i[3], i[4], i[5], i[6], i[0])
