from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__)

@app.route('/process-image', methods=['POST'])
def process_image():
    # Retrieve the image file from the request
    file = request.files.get('image')
    if not file:
        return jsonify({'error': 'No image provided'}), 400
    
    # Convert image to PIL format for processing
    img = Image.open(io.BytesIO(file.read()))

    # Image processing logic (example: get image dimensions)
    width, height = img.size
    # You can add more processing here (e.g., object detection, color analysis, etc.)
    
    # Return processed result as JSON
    result = {
        'width': width,
        'height': height,
        'message': 'Image processed successfully'
    }
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Accessible from any IP, runs on port 5000
