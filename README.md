# Library Management System

A library management system built with **Python**, **Django**, and **Django REST Framework**. It lets librarians manage books and members, issue and return books, and exposes the same functionality through a secured REST API.

## Features

- User login and logout
- Dashboard with library statistics
- Add, edit, delete, and search books
- Add, edit, and delete members
- Issue books to members and process returns
- Track borrowed and returned books
- Automatic book availability updates
- Form validation (duplicate ISBN, duplicate member email, phone number format)
- REST API with authentication and permissions
- Full CRUD through the API

## Tech Stack

| Layer     | Technology                      |
| --------- | ------------------------------- |
| Language  | Python                          |
| Framework | Django, Django REST Framework   |
| Database  | SQLite                          |
| Frontend  | HTML, CSS (Django templates)    |
| Tools     | Git, GitHub                     |

## Project Structure

```
library-management-system/
├── config/                 # Project settings and root URL configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── library/                # Main application
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Database Models

**Book**
- Title
- Author
- ISBN
- Published date
- Availability

**Member**
- Name
- Email
- Phone
- Joined date

**Borrow**
- Member (foreign key)
- Book (foreign key)
- Borrowed date
- Returned date

## REST API

All endpoints require authentication.

### Books

| Method | Endpoint            | Description         |
| ------ | ------------------- | ------------------- |
| GET    | `/api/books/`       | List all books      |
| POST   | `/api/books/`       | Create a book       |
| GET    | `/api/books/<id>/`  | Retrieve a book     |
| PUT    | `/api/books/<id>/`  | Update a book       |
| PATCH  | `/api/books/<id>/`  | Partially update    |
| DELETE | `/api/books/<id>/`  | Delete a book       |

### Members

| Method | Endpoint              | Description          |
| ------ | --------------------- | -------------------- |
| GET    | `/api/members/`       | List all members     |
| POST   | `/api/members/`       | Create a member      |
| GET    | `/api/members/<id>/`  | Retrieve a member    |
| PUT    | `/api/members/<id>/`  | Update a member      |
| PATCH  | `/api/members/<id>/`  | Partially update     |
| DELETE | `/api/members/<id>/`  | Delete a member      |

### Borrows

| Method | Endpoint                       | Description              |
| ------ | ------------------------------ | ------------------------ |
| GET    | `/api/borrows/`                | List all borrow records  |
| POST   | `/api/borrows/`                | Issue a book             |
| GET    | `/api/borrows/<id>/`           | Retrieve a borrow record |
| PUT    | `/api/borrows/<id>/`           | Update a borrow record   |
| PATCH  | `/api/borrows/<id>/`           | Partially update         |
| DELETE | `/api/borrows/<id>/`           | Delete a borrow record   |
| POST   | `/api/borrows/<id>/return/`    | Return a borrowed book   |

## Getting Started

### Prerequisites

- Python 3.10 or newer
- Git

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Prajwal-shetty-27/library-management-system.git
   cd library-management-system
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   ```

   Windows (PowerShell):
   ```powershell
   .\venv\Scripts\activate
   ```

   macOS / Linux:
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

Open <http://127.0.0.1:8000/> in your browser. The admin panel is at <http://127.0.0.1:8000/admin/>.

## Business Rules

- A book's availability updates automatically when it is issued or returned.
- An unavailable book cannot be issued.
- ISBNs and member emails must be unique.
- Member phone numbers are validated.
- Borrowing and returning work through both the web interface and the REST API.

## Key Concepts Demonstrated

- Django MVT architecture
- Models, ForeignKey relationships, and the ORM
- ModelForms and form validation
- Authentication and `login_required` views
- Django Admin
- Django REST Framework: serializers, `APIView`, authentication, permissions, status codes

## Notes

This project is intended for learning and development use. Before deploying it, set `DEBUG = False`, move `SECRET_KEY` to an environment variable, and configure `ALLOWED_HOSTS`.

## Author

**Prajwal**
GitHub: [@Prajwal-shetty-27](https://github.com/Prajwal-shetty-27)
