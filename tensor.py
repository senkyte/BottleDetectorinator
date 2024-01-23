from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st
import numpy as np

st.title("BottleRecogniserInator!")
st.header("More about the BottleRecogniserInator")
st.markdown("This image recognition was training in Teachable Machine, and TensorFlow is used for the code.")


from PIL import Image
import io
def bytesio_to_png(bytesio):
    # Seek to the beginning of the BytesIO object
    bytesio.seek(0)
    
    # Open the image using Pillow
    img = Image.open(bytesio)
    
    # Convert to PNG format
    png_data = io.BytesIO()
    img.save(png_data, format='PNG')
    
    # Seek to the beginning of the PNG data
    png_data.seek(0)
    
    return png_data

img_file = st.camera_input("Take a picture")

if img_file is not None: # Why is this a condition? Because Streamlit would constantly refresh and run the code, leading to a really ugly error that appears when no input is given, and is treated as None type. Adjust all codes accordingly.
    img_file = bytesio_to_png(img_file)
    # This code is credited to Teachable Machine
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("/Users/alexanderkoh/Downloads/python2/keras_model.h5", compile=False)

    # Load the labels
    class_names = open("/Users/alexanderkoh/Downloads/python2/labels.txt", "r").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(img_file).convert("RGB")
    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    st.write("Class:", class_name[2:], end="")
    st.write("Confidence Score:", confidence_score)

    # Here is where the Teachable Machine code ends.
