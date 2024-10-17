import requests

# URL of the laptop's Flask server
url = 'http://192.168.43.120:5000/process-image'  # Replace <laptop_ip> with the actual IP of the laptop

# Path to the image file on the Raspberry Pi
image_path = 'path/to/your/image.jpg'

# Open the image file in binary mode
with open(image_path, 'rb') as img_file:
    # Send a POST request with the image file
    files = {'image': img_file}
    response = requests.post(url, files=files)
    
    # Check the response status
    if response.status_code == 200:
        # If successful, print the JSON response from the laptop
        print('Response from laptop:', response.json())
    else:
        print('Error:', response.status_code, response.text)
