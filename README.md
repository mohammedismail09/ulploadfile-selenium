📁 Django File Upload System with Selenium Testing:
- A simple Django-based web application that allows users to sign up, log in, and upload files. The app includes role-based redirects and file download options, along with Selenium automation scripts to test the signup, login, and file upload workflows.


📌 FEATURES:
- User registration with role selection (User/Admin)
- Secure login with role-based redirects:
    - Admin → File List page
    - User → Upload page
- File upload functionality (supports any file type)
- File download option for uploaded files (for Admin)
- Automated browser testing using Selenium


🚀 TECH STACK:
- Python 3
- Django
- PostgreSQL
- Selenium
- HTML
- ChromeDriver (for Selenium)


⚙️ SETUP INSTRUCTIONS:
1. Clone the repository
- git clone https://github.com/yourusername/your-repo-name.git
- cd your-repo-name

2. Create a virtual environment and activate
- python -m venv venv
- venv\Scripts\activate  # Windows

3. Install dependencies
- pip install -r requirements.txt
- If no requirements.txt, install manually: pip install django selenium

4. Run migrations
- python manage.py migrate

5. Start the development server
- python manage.py runserver

6. Open Selenium Test (in another terminal)
- python testing.py


🔍 NOTES:
- Ensure ChromeDriver path is correctly set in testing.py
- Media files will be uploaded to /media/uploads/
- Make sure to create a media/ folder before running the server
- Adjust file paths in testing.py based on your local system


📜 LICENSE:
- MIT License — free to use and modify.


✨ AUTHOR:
- Mohammed Ismail Ahmed
- GitHub: @mohammedismail09