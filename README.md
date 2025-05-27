
# SnugStitch

SnugStitch is a web-based application designed to streamline the process of discovering and managing fashion apparel. This project provides a user-friendly interface for browsing, selecting, and organizing clothing items, with support for various categories such as T-shirts, women's wear, and more.

## Features

- Clean and intuitive user interface
- Dynamic templates for different product categories
- Backend integration for handling product data
- Responsive layout for desktop and mobile devices
- Easily extendable to support more product types or features

## Technologies Used

- HTML, CSS, JavaScript
- Python (Flask)
- Jinja2 Templates
- Bootstrap (optional, if used)

## Folder Structure



SnugStitch/

├── static/                # CSS, JS, and image assets

├── templates/ 

│      ├── index.html

│      ├── menstshirts.html

│      └── womenstshirts.html

├── app.py                 # Main Flask application

└── README.md              # Project documentation



## Getting Started

1. Clone the repository:

   git clone https://github.com/Mandadapu-Kinnera/SnugStitch.git
   cd SnugStitch


2. Set up a virtual environment and install dependencies:

 
   python -m venv venv
   venv\Scripts\activate    # On Windows
   pip install -r requirements.txt
   

3. Run the Flask app:

  
   python app.py
  

4. Visit `http://127.0.0.1:5000/` in your browser to view the app.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute it for personal or commercial purposes.

## Author

Developed by Mandadapu Kinnera.

