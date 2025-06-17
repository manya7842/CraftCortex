from flask import Flask, request, render_template
import numpy as np
import cv2
import pickle
import os

from tensorflow.keras.models import load_model
from tensorflow.keras.layers import InputLayer
from tensorflow.keras.utils import get_custom_objects
from werkzeug.utils import secure_filename

# Import your custom search functions
from youtube_search import search_youtube_tutorial
from pinterest_search import search_pinterest_tutorial


def custom_input_layer(config, **kwargs):
    input_config = config.copy()
    if 'batch_shape' in input_config:
        batch_shape = input_config.pop('batch_shape')
        # Extract the shape (excluding the batch dimension)
        if batch_shape is not None and len(batch_shape) > 1:
            input_config['shape'] = tuple(batch_shape[1:])
    return InputLayer(**input_config)

get_custom_objects().update({
    'InputLayer': lambda **kwargs: custom_input_layer(kwargs)
})

# Load the trained model
model = load_model('CraftCortex.h5')
print("✅ Model loaded successfully!")

# Initialize Flask app
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load your label encoder
with open('label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

# Function to preprocess uploaded image
def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (128, 128))  # Adjust to your model input size
    img = img / 255.0
    return np.expand_dims(img, axis=0)

# Route to handle upload and prediction
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    prediction = None
    youtube_links = []
    pinterest_links = []

    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            # Preprocess and predict
            processed_img = preprocess_image(filepath)
            pred = model.predict(processed_img)
            predicted_class_num = np.argmax(pred)
            prediction = label_encoder.inverse_transform([predicted_class_num])[0]

            # Get relevant tutorials
            youtube_links = search_youtube_tutorial(prediction)
            pinterest_links = search_pinterest_tutorial(prediction)

    return render_template('index.html',
                           prediction=prediction,
                           youtube_links=youtube_links,
                           pinterest_links=pinterest_links)

# Start the Flask server
if __name__ == '__main__':
    app.run(debug=True)