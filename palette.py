from skimage import exposure
from scipy.spatial.distance import cdist
import numpy as np
from sklearn.cluster import KMeans
from PIL import Image
from skimage import color



def extract_color_palette(img_np, numnode=6):
    if numnode > 6:
        numnode = 6
    
    pixels = img_np.reshape(-1, 3)
      
    kmeans = KMeans(n_clusters=numnode, random_state=42)
    kmeans.fit(pixels)

    
    colors = kmeans.cluster_centers_.astype(int)

    labels = kmeans.labels_

    return colors, labels

import numpy as np
from skimage import color

def smooth_recolor(img_np, old_color, new_color, sigma=8):

    img_lab = color.rgb2lab(img_np / 255.0)
    old_lab = color.rgb2lab(np.array([[old_color]]) / 255.0)[0, 0]
    new_lab = color.rgb2lab(np.array([[new_color]]) / 255.0)[0, 0]

    # LAB distance map
    dist = np.linalg.norm(img_lab - old_lab, axis=-1)
    weights = np.exp(-(dist**2) / (2 * sigma**2))

    # Apply weighted shift
    shift = new_lab - old_lab
    img_lab += weights[..., np.newaxis] * shift

    recolored = color.lab2rgb(img_lab)
    return np.clip(recolored * 255, 0, 255).astype(np.uint8)



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
    matched = exposure.match_histograms(img_np, recolored_img, channel_axis=-1)
    return np.clip(matched, 0, 255).astype(np.uint8)
