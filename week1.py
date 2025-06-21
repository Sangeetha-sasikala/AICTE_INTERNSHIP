import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import classification_report, confusion_matrix

# Step 2: Define Paths
base_dir = 'C:\Users\admin\AICTE-Internship\P4 - Garbage Classification​​\garbage\TrashType_Image_Dataset'  # Replace with your dataset folder name if different
img_size = 224
batch_size = 32