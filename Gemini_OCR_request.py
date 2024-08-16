import requests
import base64

# Replace 'your_api_key' with your actual Gemini API key
API_KEY = 'your_api_key'
API_URL = 'https://api.gemini.com/v1/text-extraction'

def extract_text_from_image(image_path):
    # Read the image file and encode it to base64
    with open(image_path, 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

    # Prepare the request payload
    payload = {
        'image': encoded_image
    }

    # Set the headers
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    # Make the request to the Gemini API
    response = requests.post(API_URL, json=payload, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the text from the response
        extracted_text = response.json().get('text', '')
        return extracted_text
    else:
        print(f"Error: {response.status_code}")
        print(response.json())
        return None

# Example usage
image_path = 'path_to_your_image.jpg'
text = extract_text_from_image(image_path)
if text:
    print("Extracted Text:")
    print(text)
else:
    print("Failed to extract text from the image.")