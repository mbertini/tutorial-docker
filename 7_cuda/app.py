from flask import Flask, request, jsonify, render_template
from model import classify_image

app = Flask(__name__)

@app.route('/')
def landing_page():
    return '''
    <!doctype html>
    <title>Upload an Image</title>
    <h1>Upload an Image for Prediction</h1>
    <form method="POST" action="/predict" enctype="multipart/form-data">
        <input type="file" name="image" accept="image/*">
        <input type="submit" value="Upload">
    </form>
    '''

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    img = request.files['image']
    label = classify_image(img)
    return jsonify({'prediction': label})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
