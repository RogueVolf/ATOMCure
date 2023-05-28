import os
import numpy as np

images = np.load("BD_Img.npy")
labels = np.load("BD_Label.npy")

from keras.models import Model
from keras.layers import Dense, Flatten, Input, Conv2D, MaxPooling2D, Dropout, concatenate, Conv2DTranspose, UpSampling2D, Activation

# Define the U-Net model architecture
def unet_model(input_shape):
    # Input layer
    inputs = Input(input_shape)
    # Contracting path
    conv1 = Conv2D(64, 3, activation='relu', padding='same')(inputs)
    conv1 = Conv2D(64, 3, activation='relu', padding='same')(conv1)
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)
    
    conv2 = Conv2D(128, 3, activation='relu', padding='same')(pool1)
    conv2 = Conv2D(128, 3, activation='relu', padding='same')(conv2)
    pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)
    
    # Skipping connection
    conv3 = Conv2D(256, 3, activation='relu', padding='same')(pool2)
    conv3 = Conv2D(256, 3, activation='relu', padding='same')(conv3)
    pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)
    
    # Expanding path
    conv4 = Conv2D(512, 3, activation='relu', padding='same')(pool3)
    conv4 = Conv2D(512, 3, activation='relu', padding='same')(conv4)
    
    # Upsampling and concatenation
    up5 = Conv2DTranspose(256, 2, strides=(2, 2), padding='same')(conv4)
    up5 = concatenate([up5, conv3], axis=3)
    conv5 = Conv2D(256, 3, activation='relu', padding='same')(up5)
    conv5 = Conv2D(256, 3, activation='relu', padding='same')(conv5)
    
    up6 = Conv2DTranspose(128, 2, strides=(2, 2), padding='same')(conv5)
    up6 = concatenate([up6, conv2], axis=3)
    conv6 = Conv2D(128, 3, activation='relu', padding='same')(up6)
    conv6 = Conv2D(128, 3, activation='relu', padding='same')(conv6)
    
    up7 = Conv2DTranspose(64, 2, strides=(2, 2), padding='same')(conv6)
    up7 = concatenate([up7, conv1], axis=3)
    conv7 = Conv2D(64, 3, activation='relu', padding='same')(up7)
    conv7 = Conv2D(64, 3, activation='relu', padding='same')(conv7)
    
    flatten = Flatten()(conv7)

    # Output layer for binary classification
    output = Dense(2,activation='softmax')(flatten)
    
    model = Model(inputs=inputs, outputs=output)
    
    return model

# Set the input shape for the U-Net model
input_shape = (256, 256, 1)  # Assuming grayscale CT scan images

# Create the U-Net model for binary classification
model = unet_model(input_shape)

# Print the summary of the U-Net model
model.summary()

import numpy as np
data_x = np.load("BD_Img.npy")
data_y = np.load("BD_Label.npy")

data_y.shape

data_y_encod = np.zeros((3000,2))
for i,y in enumerate(data_y):
    data_y_encod[i][y]=1
data_y_encod.shape
data_y_encod[0]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(data_x,data_y_encod,test_size=0.2)
from keras.optimizers import Adam
from keras.losses import CategoricalCrossentropy

model.compile(optimizer=Adam(learning_rate=1e-4),loss=CategoricalCrossentropy(),metrics=['accuracy'])
model.fit(x_train,y_train,batch_size=32,epochs=1,validation_split=0.2)
model.evaluate(x_test,y_test)
model.save("brain_tumor_v1")