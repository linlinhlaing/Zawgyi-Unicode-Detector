from flask import Flask, jsonify, render_template, request
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re
import numpy as np
import pickle

app = Flask(__name__)
model = tf.keras.models.load_model('zawgyi_unicode_model.h5')
with open('tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

max_length = 4182

def preprocess_input(input_text):
    text = re.sub(r"([^\s])", r"\1 ", input_text)  # Add space after each character
    sequences = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(sequences, maxlen=max_length, truncating='post', padding='post')
    return padded

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    try:
        input_text = request.json.get('text-input')
        if not input_text:
            return jsonify({'error': 'No text provided'}), 400

        padded_input = preprocess_input(input_text)
        prediction = model.predict(padded_input)
        encoding = 'Unicode' if prediction[0][0] == 1 else 'Zawgyi'# Class prediction
        

        return jsonify({'result': encoding})
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return a 500 error for server issues

if __name__ == '__main__':
    app.run(debug=True, port=5001)
