import numpy as np
from sklearn.cluster import KMeans

def extract_color_palette(img_np):
  
    pixels = img_np.reshape(-1, 3)

    numnode = len(img_np)/200
    if numnode < 3:
      numnode = 3:
    if numnode > 6:
      numnode = 6:
      
    kmeans = KMeans(n_clusters=numnode, random_state=42)
    kmeans.fit(pixels)

    
    colors = kmeans.cluster_centers_.astype(int)

    labels = kmeans.labels_

    return colors, labels
