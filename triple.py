# histogram (Convert palette)

from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
from skimage import exposure  # NEW

# Load the images]

# ---- Replace recolor_clusters with histogram matching ----
##########################################################################
def match_histograms_color(source_img, reference_img):
    matched = exposure.match_histograms(source_img, reference_img, channel_axis=-1)
    return np.clip(matched, 0, 255).astype(np.uint8)
#################################################################################
# Apply histogram matching

# Clustering Vectorshift (Naive Conversion)

import numpy as np
####################################################################
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
    return recolored_img
###################################################################
# Combined (Aliasing and Shadows)

from skimage import exposure
from scipy.spatial.distance import cdist
import numpy as np
from sklearn.cluster import KMeans
from PIL import Image

def extract_color_palette(img_np, numnode=6):
    if numnode > 6:
        numnode = 6
    
    pixels = img_np.reshape(-1, 3)
      
    kmeans = KMeans(n_clusters=numnode, random_state=42)
    kmeans.fit(pixels)

    
    colors = kmeans.cluster_centers_.astype(int)

    labels = kmeans.labels_

    return colors, labels

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