import customtkinter
from tkinter import PhotoImage
from PIL import Image

width = 1280
height = 720
nameOfApp = "Keybi"
iconPath = "content/keyboard.png"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title(nameOfApp)
        self.geometry(f"{width}x{height}")
        self.resizable(width=False, height= False)
        icon = PhotoImage(file=iconPath)
        self.iconphoto(True, icon)

my_image = customtkinter.CTkImage(light_image=Image.open(iconPath),
                                  dark_image=Image.open(iconPath),
                                  size=(30, 30))

image_label = customtkinter.CTkLabel(App.tk, image=my_image, text="")  # display image with a CTkLabel       

app = App()
app.mainloop()