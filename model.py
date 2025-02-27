import tensorflow as tf
import keras
from keras import models, layers
import matplotlib.pyplot as plt
import numpy as np

# Constants
IM_SIZE = 256
B_SIZE = 32
CHANNELS = 3
EPOCHS = 50

# Load the data
dataset = keras.preprocessing.image_dataset_from_directory(
    "PlandVillage",
    shuffle = True,
    image_size = (IM_SIZE, IM_SIZE),
    batch_size = B_SIZE
)

class_names = dataset.class_names

# Visualize the data
plt.figure(figsize=(10, 10))
for images, labels in dataset.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(class_names[labels[i]])
        plt.axis("off")
        
# Preprocess the data

train_size = 0.8
len(dataset)*train_size
train_ds = dataset.take(54)
test_ds = dataset.skip(54)

val_size = 0.1
len(dataset)*val_size
val_ds = test_ds.take(6)
test_ds = test_ds.skip(6)



