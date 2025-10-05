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
        self.grid_rowconfigure(0, weight=1)
        # Load and display image
        self.img = None
        # self.img = self.img.resize((400, 300))
        self.open_file_button = ctk.CTkButton(self, text="Open Image", command=self.open_image)
        self.open_file_button.grid(row=1, column=0, sticky="nsew")

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
        # self.img_label.place(relx=.5, rely=.5, anchor=ctk.CENTER, relwidth=.6, relheight=.6)
        self.img_label.grid(row=0, column=0, sticky="nswe")

    def update_image(self, updated_img_arr):
        self.pil_img = Image.fromarray(updated_img_arr)
        self.img = ctk.CTkImage(light_image=self.pil_img,
                                dark_image=self.pil_img,
                                size=(600, 400))
        self.img_label = ctk.CTkLabel(self, image=self.img, text="")        pass
        

class ButtonFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.current_color = None

        # Button to open color picker
        self.pick_button = ctk.CTkButton(
            self,
            text="Pick a Color",
            command=self.open_color_picker,
            fg_color="green",
        )
        self.pick_button.pack(pady=20, padx=20, fill="x")

    def open_color_picker(self):
        # Open color picker with current color
        pick_color = AskColor()
        color = pick_color.get()

        if color:
            self.current_color = color  # store chosen color

            # Update button's color
            self.pick_button.configure(fg_color=self.current_color)


class App(ctk.CTk):
    def __init__(self):
        # initialize
        super().__init__()
        self.title("Image + Color Picker Button Example")
        self.geometry("1280x720")
        self.resizable(False, False)

        # Layout
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Frames
        self.image_frame = ImageFrame(self)  # replace with your image fil
        self.image_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.button_frame = ButtonFrame(self)
        self.button_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()
