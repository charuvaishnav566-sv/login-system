# 🔐 FOSSEE Login System

A secure backend application built using **Django REST Framework** that provides JWT-based authentication and user-specific file management. The project allows users to register, log in, manage their profile, and securely upload and access their own files using PostgreSQL as the database.

---

# ✨ Features

- 👤 User Registration
- 🔑 JWT Authentication (Login)
- 🙍 Retrieve Logged-in User Details
- 📁 Upload Files
- 📋 View Uploaded Files
- 📥 Download Files
- 🗑️ Delete Files
- 🛡️ Protected API Endpoints
- ⚙️ Django Admin Panel
- 🐘 PostgreSQL Database Integration

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Django | Backend Framework |
| Django REST Framework | REST API Development |
| Simple JWT | Authentication |
| PostgreSQL | Database |
| SQLite | Used during initial development |

---

# 📂 Project Structure

```
fossee-login-system/
│
├── accounts/          # User authentication and profile
├── storage/           # File upload and management
├── config/            # Project configuration
├── media/             # Uploaded files
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🚀 Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/fossee-login-system.git
cd fossee-login-system
```

---

## 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

Activate it (Windows):

```bash
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure PostgreSQL

Update your database credentials in **config/settings.py**

Example:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "fossee_db",
        "USER": "postgres",
        "PASSWORD": "YOUR_PASSWORD",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

---

## 5️⃣ Apply Migrations

```bash
python manage.py migrate
```

---

## 6️⃣ Create an Admin User

```bash
python manage.py createsuperuser
```

---

## 7️⃣ Start the Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

# 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/register/` | Register a new user |
| POST | `/api/login/` | Login and receive JWT tokens |
| GET | `/api/me/` | Get authenticated user details |
| POST | `/api/upload/` | Upload a file |
| GET | `/api/files/` | List uploaded files |
| GET | `/api/files/<id>/` | View/Download a file |
| DELETE | `/api/files/<id>/delete/` | Delete a file |

---

# 🔐 Authentication Flow

1. Register a new account.
2. Login using `/api/login/`.
3. Copy the **Access Token** returned by the API.
4. In Postman, choose **Authorization → Bearer Token**.
5. Paste the Access Token to access protected endpoints.

---

# 📸 Testing

The APIs can be tested using:

- Postman
- Django REST Framework Browsable API

---

# 🌱 Future Enhancements

- 📧 Email Verification
- 🔒 Password Reset
- ☁️ Cloud Storage Integration
- 🐳 Docker Support
- 📝 API Documentation (Swagger/OpenAPI)
- 🧪 Automated Unit Tests

---

# 👩‍💻 Author

**Charushree Vaishnav**

Developed as part of the **FOSSEE Internship Assignment**.

---

⭐ *Thank you for reviewing this project!*
