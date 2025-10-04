from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
import pandas as pd
import seaborn as sns
    # Load the image

img_1 = Image.open("jayce.jpg").convert('RGB')
img_2 = Image.open("pussy.png").convert('RGB')
img_np_1 = np.array(img_1)
img_np_2 = np.array(img_2)

def extract_color_palette(img_np):
  
    pixels = img_np.reshape(-1, 3)

    numnode = 6
    kmeans = KMeans(n_clusters=numnode, random_state=42)
    kmeans.fit(pixels)

    colors = kmeans.cluster_centers_.astype(int)
    labels = kmeans.labels_
    arr = [colors, labels]
    return arr

new_arr_1 = extract_color_palette(img_np_1)
new_arr_2 = extract_color_palette(img_np_2)

def recolor_clusters(img_np, labels, palette_old, palette_new): 
    H, W, C = img_np.shape
    pixels = img_np.reshape(-1, 3).astype(float)
    print(len(palette_new))
    for k in range(len(palette_new)):
        # Compute shift vector for this cluster
        shift = palette_new[k] - palette_old[k]
        # Apply shift to all pixels in this cluster
        pixels[labels == k] += shift
    
    # Clip values to valid range
    pixels = np.clip(pixels, 0, 255)
    
    # Reshape back to original image shape
    recolored_img = pixels.reshape(H, W, C).astype(np.uint8)
    return recolored_img

colour = [[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255]]
print(new_arr_2[0])
image_gray = Image.fromarray(recolor_clusters(img_np_1, new_arr_1[1], new_arr_1[0], new_arr_2[0]))
image_gray.show()

