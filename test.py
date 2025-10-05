import customtkinter as ctk
from CTkColorPicker import AskColor

def ask_color():
    """Opens a color picker dialog and applies the selected color."""
    pick_color = AskColor()  # Open the color picker dialog
    color = pick_color.get() # Get the color string
    
    if color:  # Check if a color was selected (not None)
        my_button.configure(fg_color=color)

root = ctk.CTk()
root.title("Color Picker Example")
root.geometry("300x200")

my_button = ctk.CTkButton(
    master=root,
    text="CHOOSE COLOR",
    text_color="black",
    command=ask_color
)
my_button.pack(padx=30, pady=20)

root.mainloop()

