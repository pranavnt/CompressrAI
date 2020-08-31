import tensorflow as tf
from flask import Flask, request
from PIL import Image
import numpy as np

app = Flask(__name__)


@app.route('/encode', methods=['POST'])
def encode():
    img = request.files['image']
    img = Image(img)
    img = np.array(img)
    img = img.flatten()
    encoder = tf.keras.models.load_model('./encoder')
    pred = encoder.predict(img)
    return pred


@app.route('/decode', methods=['POST'])
def decode():
    img = request.files['image']
    img = Image(img)
    img = np.array(img)
    img = img.flatten()
    decoder = tf.keras.models.load_model('./decoder')
    pred = decoder.predict(img)
    return pred


app.run(debug=True, port=3418, host='localhost')
