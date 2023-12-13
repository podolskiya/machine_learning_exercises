import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import codecademylib3
import matplotlib.pyplot as plt


faces_standardized = pd.read_csv('./faces_standardized.csv').values


pca = PCA(n_components=40) 
pca.fit(faces_standardized)
eigenfaces = pca.components_ 

fig = plt.figure(figsize=(10, 8))
fig.suptitle('Eigenvectors of Images (Eigenfaces)')
for i in range(15):
    ax = fig.add_subplot(3, 5, i + 1, xticks=[], yticks=[])
    ax.set_title(f'Eigenface: #{i}')
    eigenface = eigenfaces[i]
    eigenface_reshaped = eigenface.reshape(64, 64)
    ax.imshow(eigenface_reshaped, cmap=plt.cm.bone)
plt.show()

# pca calculated
principal_components = pca.transform(faces_standardized) 

# Reconstruction of images in the original size
faces_reconstructed = pca.inverse_transform(principal_components)
fig = plt.figure(figsize=(10, 8))
