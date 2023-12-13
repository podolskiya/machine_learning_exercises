import numpy as np
from sklearn import datasets
import codecademylib3
import matplotlib.pyplot as plt

faces = datasets.fetch_olivetti_faces()['data']
faces_mean = faces.mean(axis=0)
faces_std = faces.std(axis=0)
faces_standardized = (faces - faces_mean) / faces_std
 
 
n_images, n_features = faces_standardized.shape
side_length = int(np.sqrt(n_features))
print(f'Number of features(pixels) per image: {n_features}')
print(f'Square image side length: {side_length}')
 
 
fig = plt.figure(figsize=(10, 8))

for i in range(15):
    ax = fig.add_subplot(3, 5, i + 1, xticks=[], yticks=[])
    ax.set_title(f'Image of Face: #{i}')
    face_image = faces_standardized[i]
    face_image_reshaped = face_image.reshape(side_length, side_length)
    ax.imshow(face_image_reshaped, cmap=plt.cm.bone)
plt.show()
