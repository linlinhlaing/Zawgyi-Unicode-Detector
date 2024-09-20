from flask import Flask,jsonify

app = Flask(__name__)
data = {
    1: {"name": "Lin Lin Hlaing", "age": 26},
    2: {"name": "Hnin Thant Yati", "age": 12}
}

@app.route('/')
def home():
    return "Hello, Flask!"

# just demo function for future predition model
@app.route('/predict', methods=['GET','POST'])
def predict():
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # app.run(debug=False, port=5000) 


