from skimage import exposure, color
import numpy as np
from sklearn.cluster import KMeans


def extract_color_palette(img_np, numnode=6):
    """
    Extracts a perceptually meaningful color palette using Lab-space KMeans.

    Input:
        img_np: HxWx3 uint8 RGB image
        numnode: desired number of clusters (max 6)
    Output:
        colors: (numnode, 3) uint8 RGB palette
        labels: flattened (H*W,) cluster labels
    """
    if numnode > 6:
        numnode = 6

    # Convert image to Lab for perceptual clustering
    img_lab = color.rgb2lab(img_np.astype(float) / 255.0)
    pixels = img_lab.reshape(-1, 3)

    kmeans = KMeans(n_clusters=numnode, random_state=42, n_init='auto')
    kmeans.fit(pixels)

    # Convert cluster centers (Lab) back to RGB for return
    centers_lab = kmeans.cluster_centers_
    centers_rgb = color.lab2rgb(centers_lab[np.newaxis, :, :])[0]
    colors = np.clip(centers_rgb * 255.0, 0, 255).astype(np.uint8)

    labels = kmeans.labels_
    return colors, labels

# smart recolouring
def smooth_recolor(img_np, palette_old, palette_new, sigma=10):
    """
    Smoothly recolors an image based on palette mapping using Lab-space distances.

    Input:
        img_np: HxWx3 uint8 RGB
        palette_old, palette_new: (n,3) uint8 RGB palettes
        sigma: controls smoothness (larger = wider color influence)
    Output:
        recolored: HxWx3 uint8 RGB
    """
    img_lab = color.rgb2lab(img_np.astype(float) / 255.0)
    orig_lab = img_lab.copy()

    for a in range(len(palette_old)):
        if not np.array_equal(palette_old[a], palette_new[a]):
            old_lab = color.rgb2lab(np.array([[palette_old[a]]]) / 255.0)[0, 0]
            new_lab = color.rgb2lab(np.array([[palette_new[a]]]) / 255.0)[0, 0]

            dist = np.linalg.norm(orig_lab - old_lab, axis=-1)
            weights = np.exp(-(dist ** 2) / (2 * sigma ** 2))

            shift = new_lab - old_lab
            img_lab += weights[..., np.newaxis] * shift

    recolored = color.lab2rgb(img_lab)
    return np.clip(recolored * 255.0, 0, 255).astype(np.uint8)

# histogram matching
def match_histograms_color(source_img, reference_img):
    matched = exposure.match_histograms(source_img, reference_img, channel_axis=-1)
    return np.clip(matched, 0, 255).astype(np.uint8)

# naive recolouring
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