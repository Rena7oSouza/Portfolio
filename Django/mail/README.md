📨 Mail Sender

Category: Django Project
📌 Description

Mail Sender is a simple email-sending web application built with Django. It allows users to:

✅ Fill a form to send emails
✅ Define subject, recipient and message
✅ Easily integrate with Gmail or other SMTP providers
💡 Features

    Form for sending emails directly via SMTP

    Email subject, recipient, and message inputs

    Easy configuration of sender credentials

    Responsive user interface

🚀 Technologies

    Python

    Django

    HTML, CSS

    Bootstrap

    SMTP

    Git

📂 Installation

    Clone the repository:

git clone https://github.com/Rena7oSouza/Portfolio.git
cd Portfolio/Django/mail

    Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

    Install dependencies:

pip install -r requirements.txt

    Run migrations (if needed):

python manage.py migrate

    Start the development server:

python manage.py runserver

Access http://127.0.0.1:8000 in your browser.

✉️ The default form uses environment variables or settings for the email sender account. Make sure to configure your credentials in settings.py or use Django's EMAIL_HOST_USER, EMAIL_HOST_PASSWORD.
🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you would like to change.
📬 Contact

GitHub
LinkedIn
Email

⭐ If you find this project useful, please star it on GitHub.
