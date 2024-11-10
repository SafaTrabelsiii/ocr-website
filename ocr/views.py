import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import pytesseract
from PIL import Image
from django.http import HttpResponse
import json

# OCR view - processes the image and extracts text
def ocr(request):
    if request.method == 'POST' and request.FILES['image']:
        uploaded_file = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_path = fs.url(filename)

        # Set the TESSDATA_PREFIX environment variable to the directory containing 'ara.traineddata' and 'eng.traineddata'
        os.environ['TESSDATA_PREFIX'] = '/home/pc/Bureau/Tesseract/'

        # Get the selected language from the form, default to English if no language is selected
        selected_language = request.POST.get('language', 'eng')  # Default is 'eng' if nothing is selected

        # Open the image
        image = Image.open(uploaded_file)

        # Perform OCR using the selected language (either 'eng' or 'ara')
        text = pytesseract.image_to_string(image, lang=selected_language)

        # Save extracted text to a .txt file
        text_filename = f"{os.path.splitext(filename)[0]}.txt"
        text_file_path = os.path.join(fs.location, text_filename)
        with open(text_file_path, 'w') as text_file:
            text_file.write(text)

        # Optionally, save a JSON file with extracted text
        json_filename = f"{os.path.splitext(filename)[0]}.json"
        json_file_path = os.path.join(fs.location, json_filename)
        with open(json_file_path, 'w') as json_file:
            json.dump({"text": text}, json_file)

        # Render the result page with extracted text and download links
        return render(request, 'ocr/ocr_result.html', {
            'text': text,
            'file_path': file_path,
            'text_filename': text_filename,
            'json_filename': json_filename,
        })
    
    return render(request, 'ocr/ocr_form.html')

# View for handling file download in .txt or .json format
def download_text(request, filename, format):
    fs = FileSystemStorage()
    # Build the correct file path using fs.location
    file_name_without_extension = os.path.splitext(filename)[0]
    file_to_download = None

    if format == 'txt':
        file_to_download = f"{file_name_without_extension}.txt"
    elif format == 'json':
        file_to_download = f"{file_name_without_extension}.json"

    # Ensure that the file exists
    file_path = os.path.join(fs.location, file_to_download)
    if not os.path.exists(file_path):
        return HttpResponse("File not found.", status=404)

    # Read the file content for download
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Return file response
    if format == 'txt':
        response = HttpResponse(file_content, content_type='text/plain')
        response['Content-Disposition'] = f'attachment; filename={file_to_download}'
    elif format == 'json':
        response = HttpResponse(file_content, content_type='application/json')
        response['Content-Disposition'] = f'attachment; filename={file_to_download}'

    return response