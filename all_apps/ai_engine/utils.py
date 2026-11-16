# The BRAIN of AI system
from PIL import Image
import numpy as np
import time
from .disease_data import (cocoa_class_names, IMPACT_COCOA, SYMPTOMS_COCOA, TREATMENTS_COCOA)
from .disease_data import (potato_tomato_class_names, IMPACT_POTATO_TOMATO, SYMPTOMS_POTATO_TOMATO, TREATMENTS_POTATO_TOMATO)
from .disease_data import (cardamom_class_names, TREATMENTS_CARDAMOM, SYMPTOMS_CARDAMOM, IMPACT_CARDAMOM)
from .apps import AiEngineConfig  # ML models loads from apps.py when Django starts

def preprocess_crop_image(image, rescale=True):  # Preparing image for DL model

    image = Image.open(image).convert("RGB")    # open image & ensures image into 3 color channel
                                                # RED,GREEN,BLUE
    image = image.resize((224, 224))            # Make the image into 224 * 224 input, So NN can handle

    image_array = np.array(image, dtype=np.float32) # converts image into matrix of numbers for represent
                                                    # for pixel brightness 
                                                    # 0 -> complate black | 255 -> max brightness

    if rescale:  # For Cardamom EfficientNetB0 model
        image_array = image_array / 255.0      # Divide every pixel value by 255.0 down to a range of
                                               # 0.0 & 1.0 to perform Normalization

    image_array = np.expand_dims(image_array, axis=0)
    
    print("Image Shape:", image_array.shape)
    return image_array


def predict_cocoa_disease(image):

    start_time = time.time()

    image_array = preprocess_crop_image(image)

    model = AiEngineConfig.COCOA_MODEL

    prediction = model.predict(image_array) # AI model reads the mathematical image, OUTPUT probabilities
                                            # like how matches trained images [0.05, 0.86, 0.45]
                                            
# My DL model is to recognize 3 different cocoa conditions, 
# 1. Healthy (Index 0)
# 2. Black Pod Rot (Index 1)
# 3. Pod Borer (Index 2)
# When you run prediction = model.predict(image_array), 
# the OUTPUT looks like a raw list of decimals: [0.05, 0.86, 0.45] 
# these outputs means 5% of Healthy | 86% of Black pod Rot | 45% Pod Borer

    model_time = round(time.time() - start_time, 3) 

    top_index = np.argmax(prediction)    # Finds the index large number of list [0.05, 0.86, 0.45]
 
    prediction_disease = cocoa_class_names[top_index] # Store class name of Datset like 
                                                      # 'Healthy' 'Black Pod Rot' 'Pod Borer'

    confidence_score = round(float(np.max(prediction) * 100),2)

    return {
        "disease": prediction_disease.replace("_", " ").title(),
        "confidence": confidence_score,
        "model_time": model_time,

        "treatment": TREATMENTS_COCOA.get(
            prediction_disease,
            "No treatment available"
        ),

        "impact": IMPACT_COCOA.get(
            prediction_disease,
            "No impact information available"
        ),

        "symptoms": SYMPTOMS_COCOA.get(
            prediction_disease,
            "No symptoms available"
        ),

    }


def predict_potato_tomato_disease(image):

    start_time = time.time()

    image_array = preprocess_crop_image(image)

    model = AiEngineConfig.POTATO_TOMATO_MODEL

    prediction = model.predict(image_array)

    model_time = round(time.time() - start_time, 3)

    top_index = np.argmax(prediction)

    prediction_disease = potato_tomato_class_names[top_index]

    confidence_score = round(float(np.max(prediction) * 100),2)

    return {
        "disease": prediction_disease.replace("_", " ").title(),
        "confidence": confidence_score,
        "model_time": model_time,

        "treatment": TREATMENTS_POTATO_TOMATO.get(
            prediction_disease,
            "No treatment available"
        ),

        "impact": IMPACT_POTATO_TOMATO.get(
            prediction_disease,
            "No impact information available"
        ),

        "symptoms": SYMPTOMS_POTATO_TOMATO.get(
            prediction_disease,
            "No symptoms available"
        ),

    }
    

def predict_cardamom_disease(image):

    start_time = time.time()

    image_array = preprocess_crop_image(image, rescale=False)

    model = AiEngineConfig.CARDAMOM_MODEL

    prediction = model.predict(image_array)

    model_time = round(time.time() - start_time, 3)

    top_index = np.argmax(prediction)

    prediction_disease = cardamom_class_names[top_index]

    confidence_score = round(float(np.max(prediction) * 100),2)

    print("Cardamom raw probabilities:", dict(zip(cardamom_class_names, prediction[0].round(3))))

    return {
        "disease": prediction_disease.replace("_", " ").title(),
        "confidence": confidence_score,
        "model_time": model_time,

        "treatment": TREATMENTS_CARDAMOM.get(
            prediction_disease,
            "No treatment available"
        ),

        "impact": IMPACT_CARDAMOM.get(
            prediction_disease,
            "No impact information available"
        ),

        "symptoms": SYMPTOMS_CARDAMOM.get(
            prediction_disease,
            "No symptoms available"
        ),

    }
