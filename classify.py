from tensorflow.keras.layers import Conv2D,Flatten,Dense,MaxPool2D,BatchNormalization,GlobalAveragePooling2D
from tensorflow.keras.applications.resnet50 import preprocess_input,decode_predictions
from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import Model
import matplotlib.pyplot as plt
import numpy as np
from keras.models import load_model
import tensorflow as tf


def classify(img):
    detect = ["Aadhar Card" , "PAN Card","Unknown"]
    img_array = image.img_to_array(img)

    img_batch = np.expand_dims(img_array, axis=0)

    img_preprocessed = preprocess_input(img_batch)
    model = load_model('KYC_verification.h5')

    prediction = model.predict(img_preprocessed)
    #print(prediction)
    preds=np.argmax(prediction)
    #print(preds)
    #print(detect[preds])

    return detect[preds]
