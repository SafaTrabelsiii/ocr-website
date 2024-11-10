# OCR Website

## Overview 
This project is an OCR (Optical Character Recognition) website built with Django. It allows users to upload images and extract text from them using OCR technology in English and Arabic. The website provides a simple interface for users to interact with the OCR tool.

## Features 
- **Image Upload:** Users can upload images for text extraction.
- **Text Extraction:** Utilizes OCR technology to extract text from the uploaded images.
- **Future Enhancements:** Plans to implement additional features, including but not limited to user authentication and other enhancements to improve user experience and functionality.

## Tech Stack 
- **Backend:** Django
- **Database:** PostgreSQL (SQLite is used for development by default, but PostgreSQL is recommended for scaling in the future, especially with user authentication).
- **Frontend:** HTML, CSS (JavaScript is not currently used, but may be added for interactive features in the future).

## Getting Started

### Prerequisites 
- Python 3.x
- PostgreSQL (optional for development, SQLite is sufficient for initial setup)
- Django

### Installation 

1. Clone the repository: 
   ```bash 
   git clone <repository_url> 
   cd ocr_website

```
2. Create a virtual environment: 
```bash
python3 -m venv venv 
source venv/bin/activate
``` 

3. Install dependencies 

``` bash 
pip install -r requirements.txt
```
4. Set up the database (optional at this stage)
- For PostgreSQL:
```bash 
sudo -u posgres psql
```
```sql 
CREATE DATABASE your_datatabase_name;
CREATE ROLE your_user_name WITH LOGIN PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_user_name;

```
Replace your_database_name, your_username, and your_password with your desired values.

5. Check permissions 
6. Apply migrations:

```bash
pyhton manage.py migrate
```
7. Run the server 
```bash 
python manage.py runserver 

## Usage
Navigate to [http://127.0.0.1:8000/ocr/](http://127.0.0.1:8000/ocr/) in your web browser to access the OCR website.


## Contributing
Feel free to submit issues or pull requests for any enhancements or bug fixes.


## Acknowledgements
Thanks to the Django community and various online resources that made this project possible.