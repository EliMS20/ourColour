import customtkinter as ctk
from PIL import Image, ImageTk
from CTkColorPicker import AskColor
from tkinter import filedialog
import numpy as np

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class ImageFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0,1), weight=1)

        self.title = ctk.CTkLabel(self,
                                  text="Image",
                                  fg_color="gray50",
                                  corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="nwe")

        # Load and display image
        self.img = None
        # self.img = self.img.resize((400, 300))
        self.open_file_button = ctk.CTkButton(self, text="Open Image", 
                                              command=self.open_image,
                                              corner_radius=6)
        self.open_file_button.grid(row=2, column=0, padx=10, pady=10, sticky="sew")

    def open_image(self):
        filepath = filedialog.askopenfilename(
            initialdir="/",
            title="Select an image",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")]
        )
        self.pil_img = Image.open(filepath)

        self.img = ctk.CTkImage(light_image=self.pil_img,
                                dark_image=self.pil_img,
                                size=(600, 400))
        self.img_label = ctk.CTkLabel(self, image=self.img, text="")
        self.img_label.place(relx=.5, rely=.5, anchor=ctk.CENTER)

    def update_image(self, updated_img_arr):
        self.pil_img = Image.fromarray(updated_img_arr)
        self.img = ctk.CTkImage(light_image=self.pil_img,
                                dark_image=self.pil_img,
                                size=(600, 400))
        self.img_label = ctk.CTkLabel(self, image=self.img, text="")
        self.img_label.place(relx=.5, rely=.5, anchor=ctk.CENTER)
        

class ButtonFrame(ctk.CTkFrame):
    def __init__(self, master, colors):
        super().__init__(master)
        self.corner_radius=6
        self.grid_columnconfigure(0, weight=1)
        self.title = ctk.CTkLabel(self,
                                  text="Colour Changers",
                                  fg_color="gray50",
                                  corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="we")
        self.current_color = None
        self.buttons = []

        # Button to open color picker
        for i in range(len(colors)):
            hex_val = f"#{colors[i][0]:02X}{colors[i][1]:02X}{colors[i][2]:02X}"
            button = ctk.CTkButton(
                self,
                text=f"Colour {i}",
                fg_color=hex_val,
                corner_radius=6
            )
            button.configure(command=lambda but=button: self.open_color_picker(but))
            button.grid(padx=10, pady=10, row=i+1, column=0, sticky="we")
        

    def open_color_picker(self, button):
        # Open color picker with current color
        pick_color = AskColor()
        color = pick_color.get()
        print(pick_color)
        print(color)

        if color:
            # Update button's color
            button.configure(fg_color=color)

            # update colour palette


class App(ctk.CTk):
    def __init__(self):
        # initialize
        super().__init__()
        self.title("Image + Color Picker Button Example")
        self.geometry("1280x720")
        self.resizable(False, False)

        # Layout
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Frames
        self.image_frame = ImageFrame(self)  # replace with your image fil
        self.image_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.button_frame = ButtonFrame(self, [[1, 2, 3]])
        self.button_frame.grid(row=0, column=0, padx=10, pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
