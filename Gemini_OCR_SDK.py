"""

conda install -c conda-forge google-generativeai

"""
import google.generativeai as genai
import os
import base64

# Replace 'your_api_key' with your actual Google API key
os.environ['GEMINI_AI_API_KEY']
API_KEY = os.environ['GEMINI_AI_API_KEY']
genai.configure(api_key=API_KEY)

def prep_image(image_path):
    # Upload the file and print a confirmation.
    sample_file = genai.upload_file(path=image_path,
                                display_name="Diagram")
    print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")
    file = genai.get_file(name=sample_file.name)
    print(f"Retrieved file '{file.display_name}' as: {sample_file.uri}")
    return sample_file

def extract_text_from_image(image_path, prompt):
    # Choose a Gemini model.
    model = genai.GenerativeModel(model_name="gemini-1.5-pro")
    # Prompt the model with text and the previously uploaded image.
    response = model.generate_content([image_path, prompt])
    return response.text

sample_file = prep_image('jetpack.jpg') 
text = extract_text_from_image(sample_file, "Extract the text in the image verbatim")
if text:
    print("Extracted Text:")
    print(text)
else:
    print("Failed to extract text from the image.")

sample_file = prep_image('jetpack2.jpg') 
text = extract_text_from_image(sample_file, "Analyze the given diagram and carefully extract the information. Include the cost of the item")
if text:
    print("Interpreted Image:")
    print(text)
else:
    print("Failed to extract text from the image.")