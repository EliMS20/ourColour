from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from skimage import exposure
from scipy.spatial.distance import cdist

# --- Load images ---
img_1 = Image.open("jayce.jpg").convert('RGB')
img_2 = Image.open("pussy.png").convert('RGB')
img_np_1 = np.array(img_1)
img_np_2 = np.array(img_2)

# --- Extract color palettes and cluster labels ---
def extract_color_palette(img_np, n_clusters=6):
    H, W, C = img_np.shape
    pixels = img_np.reshape(-1, 3)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(pixels)
    colors = kmeans.cluster_centers_.astype(int)
    labels = kmeans.labels_.reshape(H, W)   # <-- fix shape here
    return colors, labels

colors_1, labels_1 = extract_color_palette(img_np_1)
colors_2, labels_2 = extract_color_palette(img_np_2)

# --- Match clusters by nearest color ---
def match_clusters(colors_src, colors_ref):
    distances = cdist(colors_src, colors_ref)
    return np.argmin(distances, axis=1)

mapping = match_clusters(colors_1, colors_2)

# --- Histogram matching per cluster (fixed) ---
def histogram_match_per_cluster(src_img, ref_img, labels_src, labels_ref, mapping):
    H, W, C = src_img.shape
    result = np.zeros_like(src_img)

    for k_src, k_ref in enumerate(mapping):
        src_mask = (labels_src == k_src)
        ref_mask = (labels_ref == k_ref)

        src_pixels = src_img[src_mask]
        ref_pixels = ref_img[ref_mask]

        if len(ref_pixels) == 0 or len(src_pixels) == 0:
            continue

        # Match each color channel separately
        matched = np.zeros_like(src_pixels)
        for c in range(3):  # RGB
            matched[:, c] = exposure.match_histograms(
                src_pixels[:, c], ref_pixels[:, c]
            )

        result[src_mask] = matched

    return np.clip(result, 0, 255).astype(np.uint8)

# --- Apply the per-cluster histogram matching ---
matched_img = histogram_match_per_cluster(img_np_1, img_np_2, labels_1, labels_2, mapping)

# --- Show results ---
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.imshow(img_np_1)
plt.title("Source (jayce.jpg)")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(img_np_2)
plt.title("Reference (pussy.png)")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(matched_img)
plt.title("Per-Cluster Histogram Match")
plt.axis("off")

plt.show()
