import cv2
import numpy as np
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input as mobilenet_v2_preprocess_input


model = tf.keras.models.load_model("saved_models/Plant_Disease_Classification.h5")

## Load file
uploaded_file = st.file_uploader("choose a image file", type="jpg")

map_dict = {0: "Corn__Common_rust",
            1: "Pepper__bell___Bacterial_spot",
            2: "Pepper__bell___healthy",
            3: "Potato___Early_blight",
            4: "Potato___Late_blight",
            5: "Potato___healthy",
            6: "Tomato_Bacterial_spot",
            7: "Tomato_Early_blight",
            8: "Tomato_Late_blight",
            9: "Tomato_Leaf_Mold",
            10: "Tomato_Septoria_leaf_spot",
            11: "Tomato_Spider_mites_Two_spotted_spider_mite",
            12: "Tomato__Target_Spot",
            13: "Tomato__Tomato_YellowLeaf__Curl_Virus",
            14: "Tomato__Tomato_mosaic_virus",
            15: "Tomato_healthy"
}


if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
    resized = cv2.resize(opencv_image,(224,224))
    # Now do something with the image! For example, let's display it:
    st.image(opencv_image, channels="RGB")

    resized = mobilenet_v2_preprocess_input(resized)
    img_reshape = resized[np.newaxis,...]

    Genrate_pred = st.button("Generate Prediction")    
    if Genrate_pred:
        prediction = model.predict(img_reshape).argmax()
        st.title("Predicted Disease for this image is {}".format(map_dict [prediction]))