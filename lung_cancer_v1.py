#2 is normal
import os
import numpy as np

from sklearn.model_selection import train_test_split
from keras.models import Model
from keras.layers import Dense, Input, Conv2D, MaxPooling2D, Dropout, concatenate, UpSampling2D, Activation, Flatten

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

    # Bottom of the U
    conv3 = Conv2D(256, 3, activation='relu', padding='same')(pool2)
    conv3 = Conv2D(256, 3, activation='relu', padding='same')(conv3)

    # Expanding path
    up4 = UpSampling2D((2, 2))(conv3)
    up4 = concatenate([up4, conv2], axis=3)
    conv4 = Conv2D(128, 3, activation='relu', padding='same')(up4)
    conv4 = Conv2D(128, 3, activation='relu', padding='same')(conv4)

    up5 = UpSampling2D((2, 2))(conv4)
    up5 = concatenate([up5, conv1], axis=3)
    conv5 = Conv2D(64, 3, activation='relu', padding='same')(up5)
    conv5 = Conv2D(64, 3, activation='relu', padding='same')(conv5)

    flatten = Flatten()(conv5)
    # Output layer for binary segmentation
    output = Dense(4, activation='softmax')(flatten)
    
    model = Model(inputs=inputs, outputs=output)
    
    return model

# Set the input shape for the U-Net model
input_shape = (460, 460, 1)  # Assuming grayscale CT scan images

# Create the U-Net model for binary segmentation
model = unet_model(input_shape)

# Print the summary of the U-Net model
data_x = np.load("LungsImg.npy")
data_y = np.load("LungsLab.npy")


data_y.shape
data_y_encod = np.zeros((928,4))
for i,y in enumerate(data_y):
    data_y_encod[i][y]=1
x_train,x_test,y_train,y_test = train_test_split(data_x,data_y_encod,test_size=0.2)
from keras.optimizers import Adam
from keras.losses import categorical_crossentropy

model.compile(optimizer=Adam(learning_rate=1e-4), loss=categorical_crossentropy, metrics=['accuracy'])
model.fit(x_train,y_train,batch_size=32,epochs=3,validation_split=0.2)
model.evaluate(x_test,y_test)