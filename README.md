\# Library Management System



A Library Management System built using Python and Django. The project allows users to manage books, members, borrowing and returning of books, authentication, and REST APIs.



\## Features



\- User Login and Logout

\- Dashboard with library statistics

\- Add, Edit, and Delete Books

\- Search Books

\- Add, Edit, and Delete Members

\- Issue Books to Members

\- Return Books

\- Track Borrowed and Returned Books

\- Book availability management

\- Form validation

\- Django REST Framework APIs

\- API authentication and permissions

\- CRUD operations through REST APIs



\## Technologies Used



\- Python

\- Django

\- Django REST Framework

\- SQLite

\- HTML

\- CSS

\- Git

\- GitHub



\## Project Structure



```text

library\_management\_system/

│

├── config/

│   ├── settings.py

│   ├── urls.py

│   ├── asgi.py

│   └── wsgi.py

│

├── library/

│   ├── migrations/

│   ├── templates/

│   ├── static/

│   ├── admin.py

│   ├── forms.py

│   ├── models.py

│   ├── serializers.py

│   ├── urls.py

│   └── views.py

│

├── manage.py

├── .gitignore

└── README.md



Database Models

The project contains three main models.

Book

Stores information about books:

\- Title

\- Author

\- ISBN

\- Published Date

\- Availability

Member

Stores library member information:

\- Name

\- Email

\- Phone

\- Joined Date

Borrow

Manages book borrowing and returning:

\- Member

\- Book

\- Borrowed Date

\- Returned Date

REST API

The project provides REST APIs for managing books, members, and borrow records.

Book APIs

GET     /api/books/

POST    /api/books/



GET     /api/books/<id>/

PUT     /api/books/<id>/

PATCH   /api/books/<id>/

DELETE  /api/books/<id>/



Member APIs

GET     /api/members/

POST    /api/members/



GET     /api/members/<id>/

PUT     /api/members/<id>/

PATCH   /api/members/<id>/

DELETE  /api/members/<id>/



Borrow APIs

GET     /api/borrows/

POST    /api/borrows/



GET     /api/borrows/<id>/

PUT     /api/borrows/<id>/

PATCH   /api/borrows/<id>/

DELETE  /api/borrows/<id>/



POST    /api/borrows/<id>/return/



Authentication

The project uses Django's built-in authentication system for user login and protected functionality.

The REST APIs use Django REST Framework authentication and permissions.

How to Run the Project

1\. Clone the repository

git clone https://github.com/Prajwal-shetty-27/library-management-system.git



2\. Navigate to the project

cd library-management-system



3\. Create a virtual environment

python -m venv venv



4\. Activate the virtual environment

For Windows PowerShell:

.\\venv\\Scripts\\activate



5\. Install dependencies

pip install django djangorestframework



6\. Apply migrations

python manage.py migrate



7\. Create a superuser

python manage.py createsuperuser



8\. Start the development server

python manage.py runserver



Open:

http://127.0.0.1:8000/



Key Django Concepts Used

\- Django MVT architecture

\- Models and ForeignKey relationships

\- Django ORM

\- ModelForms

\- Form validation

\- Authentication

\- Login required views

\- CRUD operations

\- Templates

\- Static files

\- Migrations

\- Django Admin

\- Django REST Framework

\- Serializers

\- APIView

\- API authentication and permissions

\- HTTP methods

\- API status codes

\- Error handling and debugging

Project Highlights

\- Book availability is automatically updated when a book is issued or returned.

\- Users cannot issue an unavailable book.

\- Duplicate ISBN and member email are validated.

\- Member phone numbers are validated.

\- Borrow and return operations are handled through both the web interface and REST APIs.

\- API endpoints are protected using authentication and permissions.

Learning Goals

This project was built to understand practical Django development, including:

\- Building a Django project from scratch

\- Understanding Django project and app structure

\- Working with models and relationships

\- Using the Django ORM

\- Creating and validating forms

\- Implementing authentication

\- Building CRUD functionality

\- Creating REST APIs

\- Using serializers

\- Handling API authentication and permissions

\- Debugging Django errors using traceback

Author

Prajwal



\### After saving



Run:



```powershell

git status



Then:

git add README.md

git commit -m "Add project README"

git push



This will update the README on your GitHub repository.

