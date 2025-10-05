import customtkinter as ctk
from PIL import Image, ImageTk
from CTkColorPicker import AskColor

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class ImageFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Load and display image
        self.img = Image.open("/home/eli/Pictures/Wallpapers/anime-style-clouds.jpg")
        # self.img = self.img.resize((400, 300))
        self.display_img = ctk.CTkImage(light_image=self.img, dark_image=self.img, size=(400,300))
        self.label = ctk.CTkLabel(self, image=self.display_img, text="")
        self.label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

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
        super().__init__()
        self.title("Image + Color Picker Button Example")
        self.geometry("650x400")

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
