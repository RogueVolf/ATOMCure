import os
import cv2
import numpy as np
from keras.layers import Input, Conv2D, BatchNormalization, Activation, MaxPooling2D, AveragePooling2D, Flatten, Dense
from keras.models import Model
from keras import layers

def resnet_block(inputs, filters, kernel_size, strides=(1, 1), activation='relu', batch_normalization=True):
    conv = Conv2D(filters=filters, kernel_size=kernel_size, strides=strides, padding='same')(inputs)
    if batch_normalization:
        conv = BatchNormalization()(conv)
    if activation:
        conv = Activation(activation)(conv)
    return conv

def create_resnet50(input_shape, num_classes):
    inputs = Input(shape=input_shape)
    
    conv1 = resnet_block(inputs, filters=64, kernel_size=(7, 7), strides=(2, 2))
    pool1 = MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding='same')(conv1)
    
    conv2_1 = resnet_block(pool1, filters=64, kernel_size=(3, 3))
    conv2_2 = resnet_block(conv2_1, filters=64, kernel_size=(3, 3))
    conv2_3 = resnet_block(conv2_2, filters=64, kernel_size=(3, 3))
    residual2 = resnet_block(pool1, filters=64, kernel_size=(1, 1), activation=None, batch_normalization=False)
    add2 = Activation('relu')(layers.add([conv2_3, residual2]))
    
    conv3_1 = resnet_block(add2, filters=128, kernel_size=(3, 3), strides=(2, 2))
    conv3_2 = resnet_block(conv3_1, filters=128, kernel_size=(3, 3))
    conv3_3 = resnet_block(conv3_2, filters=128, kernel_size=(3, 3))
    residual3 = resnet_block(add2, filters=128, kernel_size=(1, 1), strides=(2, 2), activation=None, batch_normalization=False)
    add3 = Activation('relu')(layers.add([conv3_3, residual3]))
    
    conv4_1 = resnet_block(add3, filters=256, kernel_size=(3, 3), strides=(2, 2))
    conv4_2 = resnet_block(conv4_1, filters=256, kernel_size=(3, 3))
    conv4_3 = resnet_block(conv4_2, filters=256, kernel_size=(3, 3))
    residual4 = resnet_block(add3, filters=256, kernel_size=(1, 1), strides=(2, 2), activation=None, batch_normalization=False)
    add4 = Activation('relu')(layers.add([conv4_3, residual4]))
    
    conv5_1 = resnet_block(add4, filters=512, kernel_size=(3, 3), strides=(2, 2))
    conv5_2 = resnet_block(conv5_1, filters=512, kernel_size=(3, 3))
    conv5_3 = resnet_block(conv5_2, filters=512, kernel_size=(3, 3))
    residual5 = resnet_block(add4, filters=512, kernel_size=(1, 1), strides=(2, 2), activation=None, batch_normalization=False)
    add5 = Activation('relu')(layers.add([conv5_3, residual5]))
    
    conv6_1 = resnet_block(add5, filters=1024, kernel_size=(3, 3), strides=(2, 2))
    conv6_2 = resnet_block(conv6_1, filters=1024, kernel_size=(3, 3))
    conv6_3 = resnet_block(conv6_2, filters=1024, kernel_size=(3, 3))
    residual6 = resnet_block(add5, filters=1024, kernel_size=(1, 1), strides=(2, 2), activation=None, batch_normalization=False)
    add6 = Activation('relu')(layers.add([conv6_3, residual6]))

        
    conv7_1 = resnet_block(add6, filters=2048, kernel_size=(3, 3), strides=(2, 2))
    conv7_2 = resnet_block(conv7_1, filters= 2048, kernel_size=(3, 3))
    conv7_3 = resnet_block(conv7_2, filters= 2048, kernel_size=(3, 3))
    residual7 = resnet_block(add6, filters= 2048, kernel_size=(1, 1), strides=(2, 2), activation=None, batch_normalization=False)
    add7 = Activation('relu')(layers.add([conv7_3, residual7]))
                      
 

    avg_pool = AveragePooling2D(pool_size=(1, 1))(add7)
    flatten = Flatten()(avg_pool)
    output = Dense(classes, activation='softmax')(flatten)
    
    model = Model(inputs=inputs, outputs=output)
    return model

# Create ResNet-50 model without pre-trained weights
input_shape = (256,256,1)  # Adjust input shape according to your data
classes = 2  # Adjust the number of classes for your classification task
model = create_resnet50(input_shape, classes)

# Compile the model with desired optimizer, loss, and metrics
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

data_x = np.load("train_img.npy")
data_y = np.load("train_labels.npy")
data_x.shape
data_y_encod = np.zeros((1400,2))
for i,y in enumerate(data_y):
    data_y_encod[i][y]=1
data_y_encod.shape
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(data_x,data_y_encod,test_size=0.2)
model.fit(x_train,y_train,batch_size=16,epochs=5,validation_split=0.2)
model.evaluate(x_test,y_test)
model.save("breast_cancer_v2")