# This code was written by Alexander Koh
# The clean bottle dataset used was gathered by Alexander Koh, and trained in Teachable Machine.
# The dirty bottle dataset was a public dataset.
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st
import numpy as np
import time
st.set_page_config(
    page_title = "The BottleDectectorInator",
    page_icon = "!",
)
st.title("BottleDetectorInator!")

st.header("More about the BottleDetectorInator")
st.markdown("This image recognition was trained in Teachable Machine, and TensorFlow is used for the code.")
st.markdown("Please take a photo of your bottle, and watch the magic happen!")


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

img_file = st.camera_input("Take a picture of the water bottle")
if img_file is not None: # Why is this a condition? Because Streamlit would constantly refresh and run the code, leading to a really ugly error that appears when no input is given, and is treated as None type. Adjust all codes accordingly.
    img_file = bytesio_to_png(img_file)
    # This portion of the code is credited to Teachable Machine
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("keras_model.h5", compile=False)

    # Load the labels
    class_names = open("labels.txt", "r").readlines()

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

  # Here is where the Teachable Machine code ends.
    if confidence_score > 0.75: #Checks the confidence score, to ensure accuracy and reliability.
        if class_name[2:-1] == "Clean": # So the text file is a tad bit annoying, therefore I have to slice some funny stuff.
            st.write("Accepted!")
        elif "Dirty" == class_name[2:-1]: 
            st.write("Your bottle is dirty! Please clean it before depositing.")
        elif class_name[2:] == "NOT A BOTTLE": 
            st.write("Invalid object! Please insert a clear plastic bottle!")
        else:
            st.write("Error code 404, I messed something up.") # A check to make sure the code is working.
    else:
        st.write("The machine is not confident, please retake the photo!")


