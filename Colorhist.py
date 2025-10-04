import numpy as np

def recolor_clusters(img_np, labels, palette_old, palette_new):

    pallette_old 
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
