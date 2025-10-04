from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
import pandas as pd
import seaborn as sns
    # Load the image


img = Image.open("jayce.jpg").convert('RGB')
img_np = np.array(img)


def extract_color_palette(img_np):
  
    pixels = img_np.reshape(-1, 3)

    numnode = 6
    kmeans = KMeans(n_clusters=numnode, random_state=42)
    kmeans.fit(pixels)

    colors = kmeans.cluster_centers_.astype(int)
    labels = kmeans.labels_
    print(colors)
    arr = [colors, labels]
    return arr

new_arr = extract_color_palette(img_np)

def recolor_clusters(img_np, labels, palette_old, palette_new): 
    H, W, C = img_np.shape
    pixels = img_np.reshape(-1, 3).astype(float)
    
    for k in range(len(palette_new)):
        # Compute shift vector for this cluster
        shift = palette_new[k] - palette_old[k]
        # Apply shift to all pixels in this cluster
        pixels[labels == k] += shift
    
    # Clip values to valid range
    pixels = np.clip(pixels, 0, 255)
    
    # Reshape back to original image shape
    recolored_img = pixels.reshape(H, W, C).astype(np.uint8)
    print(recolored_img.tolist())
    return recolored_img

colour = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
recolor_clusters(img_np, new_arr[1], new_arr[0], colour)
