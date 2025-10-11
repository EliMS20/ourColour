import customtkinter as ctk
from PIL import Image, ImageTk
from CTkColorPicker import AskColor
from tkinter import filedialog
import numpy as np
import palette as pal
import estimate
import brightness

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class ImageFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.app = master
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
        self.open_file_button.grid(row=10, column=0, padx=10, pady=10, sticky="sew")


        self.no_input_img = ctk.CTkImage(light_image=Image.open("transparent-folder.png"),
                                         size=(200, 200))
        self.no_input_img_disp = ctk.CTkLabel(self,
                                              text="",
                                              image=self.no_input_img)
        self.no_input_img_disp.place(relx=.5, rely=.5, anchor=ctk.CENTER)

        # error message
        self.error_label = None

        # image label
        self.img_label = None

    def open_image(self):
        if self.error_label:
            self.error_label.destroy()

        if self.app.toggle_frame.currently_toggled == None:
            self.error_label = ctk.CTkLabel(self,
                                            text="Error: Must select an algorithm",
                                            fg_color="red",
                                            corner_radius=6)
            self.error_label.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
            return
        
        if self.app.toggle_frame.currently_toggled == "Histogram":
            filepath1 = filedialog.askopenfilename(
                initialdir="/",
                title="Select an image",
                filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")]
            )
            filepath2 = filedialog.askopenfilename(import customtkinter as ctk
from PIL import Image, ImageTk
from CTkColorPicker import AskColor
from tkinter import filedialog
import numpy as np
import palette as pal
import estimate

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class ImageFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.app = master
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
        self.open_file_button.grid(row=10, column=0, padx=10, pady=10, sticky="sew")


        self.no_input_img = ctk.CTkImage(light_image=Image.open("transparent-folder.png"),
                                         size=(200, 200))
        self.no_input_img_disp = ctk.CTkLabel(self,
                                              text="",
                                              image=self.no_input_img)
        self.no_input_img_disp.place(relx=.5, rely=.5, anchor=ctk.CENTER)

        # error message
        self.error_label = None

        # image label
        self.img_label = None

    def open_image(self):
        if self.error_label:
            self.error_label.destroy()

        if self.app.toggle_frame.currently_toggled == None:
            self.error_label = ctk.CTkLabel(self,
                                            text="Error: Must select an algorithm",
                                            fg_color="red",
                                            corner_radius=6)
            self.error_label.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
            return
        
        if self.app.toggle_frame.currently_toggled == "Histogram":
            filepath1 = filedialog.askopenfilename(
                initialdir="/",
                title="Select an image",
                filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")]
            )
            filepath2 = filedialog.askopenfilename(
                initialdir="/",
                title="Select an image",
                filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")]
            )

            if filepath1 and filepath2:
                img1 = Image.open(filepath1)
                img1 = img1.convert("RGB")
                img1_arr = np.array(img1)
                img2 = Image.open(filepath2)
                img2 = img2.convert("RGB")
                img2_arr = np.array(img2)
                histed_img = pal.match_histograms_color(img1_arr, img2_arr)
                pil_img = Image.fromarray(histed_img)

                img = ctk.CTkImage(light_image=pil_img,
                        dark_image=pil_img,
                        size=(600, 400))
                
                self.img_label = ctk.CTkLabel(self, image=img, text="")
                self.img_label.place(relx=.5, rely=.5, anchor=ctk.CENTER)
                self.no_input_img_disp.destroy()

                self.app.button_frame.clear_buttons()

                self.app.button_frame.reset_but.configure(state="disabled")
                self.app.button_frame.reset_but.grid(row=12, column=0, padx=10, pady=10, sticky="ew", columnspan=3)
                self.app.button_frame.set_color_but.configure(state="disabled")        
                self.app.button_frame.set_color_but.grid(row=11, column=0, padx=10, pady=10, sticky="ew",columnspan=3)

                return
            else:
                return
        
        filepath = filedialog.askopenfilename(
            initialdir="/",
            title="Select an image",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")]
        )

        if filepath:
            self.pil_img = Image.open(filepath)
            self.pil_img = self.pil_img.convert("RGB")

            self.img = ctk.CTkImage(light_image=self.pil_img,
                                    dark_image=self.pil_img,
                                    size=(600, 400))
            self.img_label = ctk.CTkLabel(self, image=self.img, text="")
            self.img_label.place(relx=.5, rely=.5, anchor=ctk.CENTER)
            
            self.app.img_arr = np.array(self.pil_img)

            self.app.img_arr_modified = self.app.img_arr.copy()
            num_nodes, reps = estimate.estimate_distinct_colors_lab(self.app.img_arr)
            self.app.color_palette, self.app.labels = pal.extract_color_palette(self.app.img_arr, num_nodes)
            
            if len(self.app.button_frame.buttons) > 0:
                self.app.button_frame.clear_buttons()
            
            self.app.button_frame.set_color_but.configure(state="normal")
            self.app.color_palette_og = self.app.color_palette.copy()
            self.app.button_frame.add_buttons(self.app.color_palette)
            self.app.color_palette_copy = self.app.color_palette.copy()
            self.no_input_img_disp.destroy()
        else:
            return


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
        self.app = master
        self.corner_radius=6
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.title = ctk.CTkLabel(self,
                                  text="Colours",
                                  fg_color="gray50",
                                  corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="we", columnspan=3)
        self.buttons = []
        self.sigma = 25

        # set sigma slider
        self.sigma_slider = ctk.CTkSlider(self,
                                              from_=1, to=50,
                                              command=self.set_sigma,
                                              number_of_steps=50)
        self.sigma_slider.grid(row=10, column=1, padx=10, pady=10, sticky="ew")

        self.sigma_title = ctk.CTkLabel(self,
                                            text="Sigma:")
        self.sigma_title.grid(row=10, column=0, padx=10, pady=10)

        self.sigma_level = ctk.CTkLabel(self,
                                        text=f"{int(self.sigma_slider.get())}",
                                        width=60)
        self.sigma_level.grid(row=10, column=2, padx=10, pady=10)

        # set colour button
        self.set_color_but = ctk.CTkButton(
            self,
            text=f"Set colours",
            corner_radius=6,
            command=self.set_colors,
            state="disabled"
        )
        self.set_color_but.grid(row=11, column=0, padx=10, pady=10, sticky="ew",columnspan=3)

        # reset button
        self.reset_but = ctk.CTkButton(
            self,
            text="Reset image",
            corner_radius = 6,
            command = self.reset_image,
            state="disabled"
        )
        self.reset_but.grid(row=12, column=0, padx=10, pady=10, sticky="ew", columnspan=3)        


    def open_color_picker(self, button):
        # Open color picker with current color
        pick_color = AskColor()
        color = pick_color.get()

        if color:
            # Update button's color
            button.configure(fg_color=color)
            button.configure(text=f"{color}")

            idx_button = self.buttons.index(button)
            # update colour palette
            color = color.lstrip('#')
            r_new = int(color[0:2], 16)
            g_new = int(color[2:4], 16)
            b_new = int(color[4:6], 16)

            new_rgb = np.array([r_new, g_new, b_new])
            self.app.color_palette_copy[idx_button] = new_rgb
            

    
    def add_buttons(self, colors):  
        
        if len(self.buttons) > 0:
            self.clear_buttons()
            self.buttons = []      # Button to open color picker

        for i in range(len(colors)):
            hex_val = f"#{colors[i][0]:02X}{colors[i][1]:02X}{colors[i][2]:02X}"
            button = ctk.CTkButton(
                self,
                text=f"{hex_val}",
                fg_color=hex_val,
                corner_radius=6
            )
            button.configure(command=lambda but=button: self.open_color_picker(but))
            button.grid(padx=10, pady=10, row=i+1, column=1, sticky="we")
            self.buttons.append(button)
        self.set_color_but.configure(state="normal")
        self.set_color_but.grid(row=11, column=0, padx=10, pady=10, sticky="ew", columnspan=3)
        self.reset_but.configure(state="normal")
        self.reset_but.grid(row=12, column=0, padx=10, pady=10, sticky="ew", columnspan=3)




    def clear_buttons(self):
        if len(self.buttons) != 0:
            for button in self.buttons:
                button.destroy()
            self.buttons = []
    
    def set_colors(self):
        if (self.app.color_palette != self.app.color_palette_copy).any():

            if self.app.toggle_frame.currently_toggled == "Smart":
                new_img_arr = pal.smooth_recolor(self.app.img_arr_modified, 
                        self.app.color_palette,
                        self.app.color_palette_copy,
                        sigma=self.sigma)
            elif self.app.toggle_frame.currently_toggled == "bright":
                new_img_arr = pal.recolor_clusters(
                        self.app.img_arr_modified, 
                        self.app.labels,
                        self.app.color_palette,
                        self.app.color_palette_copy)
            
            self.app.color_palette = self.app.color_palette_copy.copy()
            self.app.image_frame.update_image(new_img_arr)
            self.app.img_arr_modified = new_img_arr

    def set_sigma(self, value):
        self.sigma = int(value)
        self.sigma_level.configure(text=f"{self.sigma}")
        
    def reset_image(self):
        self.app.image_frame.update_image(self.app.img_arr)
        self.app.img_arr_modified = self.app.img_arr.copy()
        self.app.color_palette = self.app.color_palette_og.copy()
        self.app.color_palette_copy = self.app.color_palette_og.copy()

        self.add_buttons(self.app.color_palette_og)

        pass


class Toggles(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.app = master

        self.grid_columnconfigure(0, weight=1)

        self.title = ctk.CTkLabel(self,
                                  text="Choose algorithm",
                                  fg_color="gray50",
                                  corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        self.bright_tog = ctk.CTkCheckBox(self, text="bright", 
                                         onvalue=1, offvalue=0)
        self.hist_tog = ctk.CTkCheckBox(self, text="Histogram", 
                                         onvalue=1, offvalue=0)
        self.smart_tog = ctk.CTkCheckBox(self, text="Smart", 
                                         onvalue=1, offvalue=0)
        
        self.bright_tog.configure(command=lambda tog=self.bright_tog: self.manage_toggles(tog))
        self.hist_tog.configure(command=lambda tog=self.hist_tog: self.manage_toggles(tog))
        self.smart_tog.configure(command=lambda tog=self.smart_tog: self.manage_toggles(tog))

        self.bright_tog.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.hist_tog.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.smart_tog.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.toggles = [self.bright_tog, self.hist_tog, self.smart_tog]

        self.smart_tog.select()
        self.currently_toggled = "Smart"
    
    def manage_toggles(self, current_tog):
        status = current_tog.get()
        if status ==0:
            self.currently_toggled = None
        elif status ==1:
            for toggle in self.toggles:
                toggle.deselect()
            current_tog.select()
            self.currently_toggled = current_tog.cget("text")
            pass
        pass


    pass

class App(ctk.CTk):
    def __init__(self):
        # initialize
        super().__init__()
        self.title("Image + Color Picker Button Example")
        self.geometry("1280x720")
        self.resizable(False, False)
        self.color_palette_og = []
        self.color_palette = []
        self.color_palette_copy = []
        self.labels = []
        self.img_arr = []
        self.img_arr_modified = []
        ctk.set_appearance_mode("dark")


        # Layout
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Frames
        self.image_frame = ImageFrame(self)  # replace with your image fil
        self.image_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew", rowspan=2)

        self.button_frame = ButtonFrame(self, [[1, 2, 3]])
        self.button_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nswe")

        self.toggle_frame = Toggles(self)
        self.toggle_frame.grid(row=1, column=0, padx=10, pady=10, sticky="we")


if __name__ == "__main__":
    app = App()
    app.mainloop()
                initialdir="/",
                title="Select an image",
                filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")]
            )

            if filepath1 and filepath2:
                img1 = Image.open(filepath1)
                img1 = img1.convert("RGB")
                img1_arr = np.array(img1)
                img2 = Image.open(filepath2)
                img2 = img2.convert("RGB")
                img2_arr = np.array(img2)
                histed_img = pal.match_histograms_color(img1_arr, img2_arr)
                pil_img = Image.fromarray(histed_img)

                img = ctk.CTkImage(light_image=pil_img,
                        dark_image=pil_img,
                        size=(600, 400))
                
                self.img_label = ctk.CTkLabel(self, image=img, text="")
                self.img_label.place(relx=.5, rely=.5, anchor=ctk.CENTER)
                self.no_input_img_disp.destroy()

                self.app.button_frame.clear_buttons()

                self.app.button_frame.reset_but.configure(state="disabled")
                self.app.button_frame.reset_but.grid(row=12, column=0, padx=10, pady=10, sticky="ew", columnspan=3)
                self.app.button_frame.set_color_but.configure(state="disabled")        
                self.app.button_frame.set_color_but.grid(row=11, column=0, padx=10, pady=10, sticky="ew",columnspan=3)

                return
            else:
                return
        
        filepath = filedialog.askopenfilename(
            initialdir="/",
            title="Select an image",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")]
        )

        if filepath:
            self.pil_img = Image.open(filepath)
            self.pil_img = self.pil_img.convert("RGB")

            self.img = ctk.CTkImage(light_image=self.pil_img,
                                    dark_image=self.pil_img,
                                    size=(600, 400))
            self.img_label = ctk.CTkLabel(self, image=self.img, text="")
            self.img_label.place(relx=.5, rely=.5, anchor=ctk.CENTER)
            
            self.app.img_arr = np.array(self.pil_img)

            self.app.img_arr_modified = self.app.img_arr.copy()
            num_nodes, reps = estimate.estimate_distinct_colors_lab(self.app.img_arr)
            self.app.color_palette, self.app.labels = pal.extract_color_palette(self.app.img_arr, num_nodes)
            
            if len(self.app.button_frame.buttons) > 0:
                self.app.button_frame.clear_buttons()
            
            self.app.button_frame.set_color_but.configure(state="normal")
            self.app.color_palette_og = self.app.color_palette.copy()
            self.app.button_frame.add_buttons(self.app.color_palette)
            self.app.color_palette_copy = self.app.color_palette.copy()
            self.no_input_img_disp.destroy()
        else:
            return


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
        self.app = master
        self.corner_radius=6
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.title = ctk.CTkLabel(self,
                                  text="Colours",
                                  fg_color="gray50",
                                  corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="we", columnspan=3)
        self.buttons = []
        self.sigma = 25

        # set sigma slider
        self.sigma_slider = ctk.CTkSlider(self,
                                              from_=1, to=50,
                                              command=self.set_sigma,
                                              number_of_steps=50)
        self.sigma_slider.grid(row=10, column=1, padx=10, pady=10, sticky="ew")

        self.sigma_title = ctk.CTkLabel(self,
                                            text="Sigma:")
        self.sigma_title.grid(row=10, column=0, padx=10, pady=10)

        self.sigma_level = ctk.CTkLabel(self,
                                        text=f"{int(self.sigma_slider.get())}",
                                        width=60)
        self.sigma_level.grid(row=10, column=2, padx=10, pady=10)

        # set colour button
        self.set_color_but = ctk.CTkButton(
            self,
            text=f"Set colours",
            corner_radius=6,
            command=self.set_colors,
            state="disabled"
        )
        self.set_color_but.grid(row=11, column=0, padx=10, pady=10, sticky="ew",columnspan=3)

        # reset button
        self.reset_but = ctk.CTkButton(
            self,
            text="Reset image",
            corner_radius = 6,
            command = self.reset_image,
            state="disabled"
        )
        self.reset_but.grid(row=12, column=0, padx=10, pady=10, sticky="ew", columnspan=3)        


    def open_color_picker(self, button):
        # Open color picker with current color
        pick_color = AskColor()
        color = pick_color.get()

        if color:
            # Update button's color
            button.configure(fg_color=color)
            button.configure(text=f"{color}")

            idx_button = self.buttons.index(button)
            # update colour palette
            color = color.lstrip('#')
            r_new = int(color[0:2], 16)
            g_new = int(color[2:4], 16)
            b_new = int(color[4:6], 16)

            new_rgb = np.array([r_new, g_new, b_new])
            self.app.color_palette_copy[idx_button] = new_rgb
            

    
    def add_buttons(self, colors):  
        
        if len(self.buttons) > 0:
            self.clear_buttons()
            self.buttons = []      # Button to open color picker

        for i in range(len(colors)):
            hex_val = f"#{colors[i][0]:02X}{colors[i][1]:02X}{colors[i][2]:02X}"
            button = ctk.CTkButton(
                self,
                text=f"{hex_val}",
                fg_color=hex_val,
                corner_radius=6
            )
            button.configure(command=lambda but=button: self.open_color_picker(but))
            button.grid(padx=10, pady=10, row=i+1, column=1, sticky="we")
            self.buttons.append(button)
        self.set_color_but.configure(state="normal")
        self.set_color_but.grid(row=11, column=0, padx=10, pady=10, sticky="ew", columnspan=3)
        self.reset_but.configure(state="normal")
        self.reset_but.grid(row=12, column=0, padx=10, pady=10, sticky="ew", columnspan=3)




    def clear_buttons(self):
        if len(self.buttons) != 0:
            for button in self.buttons:
                button.destroy()
            self.buttons = []
    
    def set_colors(self):
        if (self.app.color_palette != self.app.color_palette_copy).any():

            if self.app.toggle_frame.currently_toggled == "Smart":
                new_img_arr = pal.smooth_recolor(self.app.img_arr_modified, 
                        self.app.color_palette,
                        self.app.color_palette_copy,
                        sigma=self.sigma)
            elif self.app.toggle_frame.currently_toggled == "bright":
                new_img_arr = pal.recolor_clusters(
                        self.app.img_arr_modified, 
                        self.app.labels,
                        self.app.color_palette,
                        self.app.color_palette_copy)
            
            self.app.color_palette = self.app.color_palette_copy.copy()
            self.app.image_frame.update_image(new_img_arr)
            self.app.img_arr_modified = new_img_arr

    def set_sigma(self, value):
        self.sigma = int(value)
        self.sigma_level.configure(text=f"{self.sigma}")
        
    def reset_image(self):
        self.app.image_frame.update_image(self.app.img_arr)
        self.app.img_arr_modified = self.app.img_arr.copy()
        self.app.color_palette = self.app.color_palette_og.copy()
        self.app.color_palette_copy = self.app.color_palette_og.copy()

        self.add_buttons(self.app.color_palette_og)

        pass


class Toggles(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.app = master

        self.grid_columnconfigure(0, weight=1)

        self.title = ctk.CTkLabel(self,
                                  text="Choose algorithm",
                                  fg_color="gray50",
                                  corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        self.bright_tog = ctk.CTkCheckBox(self, text="bright", 
                                         onvalue=1, offvalue=0)
        self.hist_tog = ctk.CTkCheckBox(self, text="Histogram", 
                                         onvalue=1, offvalue=0)
        self.smart_tog = ctk.CTkCheckBox(self, text="Smart", 
                                         onvalue=1, offvalue=0)
        
        self.bright_tog.configure(command=lambda tog=self.bright_tog: self.manage_toggles(tog))
        self.hist_tog.configure(command=lambda tog=self.hist_tog: self.manage_toggles(tog))
        self.smart_tog.configure(command=lambda tog=self.smart_tog: self.manage_toggles(tog))

        self.bright_tog.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.hist_tog.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.smart_tog.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.toggles = [self.bright_tog, self.hist_tog, self.smart_tog]

        self.smart_tog.select()
        self.currently_toggled = "Smart"
    
    def manage_toggles(self, current_tog):
        status = current_tog.get()
        if status ==0:
            self.currently_toggled = None
        elif status ==1:
            for toggle in self.toggles:
                toggle.deselect()
            current_tog.select()
            self.currently_toggled = current_tog.cget("text")
            pass
        pass


    pass

class App(ctk.CTk):
    def __init__(self):
        # initialize
        super().__init__()
        self.title("Image + Color Picker Button Example")
        self.geometry("1280x720")
        self.resizable(False, False)
        self.color_palette_og = []
        self.color_palette = []
        self.color_palette_copy = []
        self.labels = []
        self.img_arr = []
        self.img_arr_modified = []
        ctk.set_appearance_mode("dark")


        # Layout
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Frames
        self.image_frame = ImageFrame(self)  # replace with your image fil
        self.image_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew", rowspan=2)

        self.button_frame = ButtonFrame(self, [[1, 2, 3]])
        self.button_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nswe")

        self.toggle_frame = Toggles(self)
        self.toggle_frame.grid(row=1, column=0, padx=10, pady=10, sticky="we")


if __name__ == "__main__":
    app = App()
    app.mainloop()
