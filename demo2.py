from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from skimage import exposure  # NEW

# Load the images
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
    return [colors, labels]

new_arr_1 = extract_color_palette(img_np_1)
new_arr_2 = extract_color_palette(img_np_2)

# ---- Replace recolor_clusters with histogram matching ----
def match_histograms_color(source_img, reference_img):
    matched = exposure.match_histograms(source_img, reference_img, channel_axis=-1)
    return np.clip(matched, 0, 255).astype(np.uint8)

# Apply histogram matching
matched_img = match_histograms_color(img_np_1, img_np_2)

# Show results
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
plt.title("Color-Matched Result")
plt.axis("off")

plt.show()
