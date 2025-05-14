from flask import Flask, request, jsonify
from model import classify_image

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    img = request.files['image']
    label = classify_image(img)
    return jsonify({'prediction': label})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
