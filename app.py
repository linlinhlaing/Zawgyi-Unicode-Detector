from flask import Flask,jsonify,render_template,request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    try:
        input_text = request.form['text-input']

        # Replace this logic with your actual model classification logic
        if input_text:  # Ensure that input_text is not empty
            encoding = 'Zawgyi'  # Dummy response for encoding
            confidence = 85.0     # Dummy confidence score
            return render_template('index.html', result=encoding, confidence= confidence)
        else:
            return jsonify({'error': 'No text provided'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return a 500 error for server issues


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    app.run(debug=False, port=5001) 


