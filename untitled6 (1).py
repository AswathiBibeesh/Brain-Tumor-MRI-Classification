# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ofUdmZjAEt1x0s56zf0Xmtsiv_estQaf
"""

# CodeGrade Tag Init1

from google.colab import drive
drive.mount('/content/drive')

import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import matplotlib.pyplot as plt
import shutil

# Define directories
train_data_dir = '/content/drive/MyDrive/Archive/Training'
test_data_dir = '/content/drive/MyDrive/Archive/Testing'

from tensorflow.keras.preprocessing.image import ImageDataGenerator
# Define classes
classes = ['glioma', 'meningioma', 'pituitary', 'no_tumor']

# ImageDataGenerator for data augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

test_datagen = ImageDataGenerator(rescale=1./255)

# Data generators
batch_size = 32

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(224, 224),  # VGG16, InceptionV3, ResNet50 require input size 224x224
    batch_size=batch_size,
    class_mode='categorical',
    classes=classes
)

test_generator = test_datagen.flow_from_directory(
    test_data_dir,
    target_size=(224, 224),
    batch_size=batch_size,
    class_mode='categorical',
    classes=classes
)

from tensorflow.keras.applications import VGG16

# Build VGG16 model from scratch
vgg16_model_scratch = Sequential([
    Conv2D(64, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(256, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(512, activation='relu'),
    Dropout(0.5),
    Dense(4, activation='softmax')  # 4 classes: glioma, meningioma, pituitary, no_tumor
])

vgg16_model_scratch.compile(loss='categorical_crossentropy',
                            optimizer='adam',
                            metrics=['accuracy'])

vgg16_model_scratch.summary()

from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D

# Load pre-trained VGG16 model without top layers
base_vgg16 = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Add custom top layers
x = base_vgg16.output
x = GlobalAveragePooling2D()(x)
x = Dense(512, activation='relu')(x)
predictions_vgg16 = Dense(4, activation='softmax')(x)

# Final model
vgg16_model_transfer = Model(inputs=base_vgg16.input, outputs=predictions_vgg16)

# Freeze the base VGG16 layers
for layer in base_vgg16.layers:
    layer.trainable = False

# Compile the model
vgg16_model_transfer.compile(optimizer='adam',
                             loss='categorical_crossentropy',
                             metrics=['accuracy'])

vgg16_model_transfer.summary()

from tensorflow.keras.applications import InceptionV3

# Load pre-trained InceptionV3 model without top layers
base_inception = InceptionV3(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Add custom top layers
x = base_inception.output
x = GlobalAveragePooling2D()(x)
x = Dense(512, activation='relu')(x)
predictions_inception = Dense(4, activation='softmax')(x)

# Final model
inception_model = Model(inputs=base_inception.input, outputs=predictions_inception)

# Freeze the base InceptionV3 layers
for layer in base_inception.layers:
    layer.trainable = False

# Compile the model
inception_model.compile(optimizer='adam',
                        loss='categorical_crossentropy',
                        metrics=['accuracy'])

inception_model.summary()

from tensorflow.keras.applications import ResNet50

# Load pre-trained ResNet50 model without top layers
base_resnet = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Add custom top layers
x = base_resnet.output
x = GlobalAveragePooling2D()(x)
x = Dense(512, activation='relu')(x)
predictions_resnet = Dense(4, activation='softmax')(x)

# Final model
resnet_model = Model(inputs=base_resnet.input, outputs=predictions_resnet)

# Freeze the base ResNet50 layers
for layer in base_resnet.layers:
    layer.trainable = False

# Compile the model
resnet_model.compile(optimizer='adam',
                     loss='categorical_crossentropy',
                     metrics=['accuracy'])

resnet_model.summary()

epochs = 20

# Train VGG16 from scratch
history_vgg16_scratch = vgg16_model_scratch.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    validation_data=test_generator,
    validation_steps=test_generator.samples // batch_size,
    epochs=epochs
)

# Train VGG16 with transfer learning
history_vgg16_transfer = vgg16_model_transfer.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    validation_data=test_generator,
    validation_steps=test_generator.samples // batch_size,
    epochs=epochs
)

# Train InceptionV3 with transfer learning
history_inception = inception_model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    validation_data=test_generator,
    validation_steps=test_generator.samples // batch_size,
    epochs=epochs
)

# Train ResNet50 with transfer learning
history_resnet = resnet_model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    validation_data=test_generator,
    validation_steps=test_generator.samples // batch_size,
    epochs=epochs
)