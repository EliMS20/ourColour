import streamlit as st
from PIL import Image
import numpy as np

st.title("ourColour")

uploaded_file = st.file_uploader("Open image")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image_array = np.array(image)
    
    # display image
    st.image(image, caption="Uploaded Image", use_container_width=True)

# returns array

# Initial RGB colors
colors = [
    [255, 0, 0],    # Red
    [0, 255, 0],    # Green
    [0, 0, 255],    # Blue
    [255, 255, 0],  # Yellow
    [255, 0, 255],  # Magenta
    [0, 255, 255]   # Cyan
]

st.write("### Click a box to change the color")

cols = st.columns(len(colors))
new_colors = []

for i, col in enumerate(cols):
    # Convert RGB to hex
    hex_color = '#%02x%02x%02x' % tuple(colors[i])
    
    # Color picker in the column
    new_hex = col.color_picker(
        label="",
        value=hex_color,
        key=f"color{i}"
    )

    
    # Convert back to RGB
    new_rgb = [int(new_hex[j:j+2], 16) for j in (1, 3, 5)]
    new_colors.append(new_rgb)

print(new_colors[3])

