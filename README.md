
# 🚀 Asset Manager Platform

A robust Django-based application for managing assets, devices, asset profiles, and device profiles. Built with PostgreSQL as the backend and designed to be scalable and extensible.

---

## 📦 Features

- CRUD operations for:
  - Assets 🏗️
  - Devices ⚙️
  - Asset Profiles 📄
  - Device Profiles 📜
- Prevents duplicate entries (no duplicates allowed!)
- Automatically creates database tables via Django migrations
- Clear modular separation between apps

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/assetManager.git
cd assetManager
```

### 2. Set Up Python Virtual Environment

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Create `.env` File

Inside your project root, create a `.env` file with the following content:

```env
DB_NAME='gateway_db'
DB_USER='postgres'
DB_PASSWORD='@Secure123!'  # Use proper escaping or no comment after `#`
DB_HOST='localhost'
DB_PORT='5432'
```

### 4. Create the Database

**Option 1: Manually (Recommended)**

Login to PostgreSQL and run:

```sql
CREATE DATABASE gateway_db;
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Server

```bash
python manage.py runserver
```

Access the admin panel at: [http://localhost:8000/admin](http://localhost:8000/admin)

---

## 📂 Project Structure

```
assetManager/
├── asset/               # Asset management app
├── device/              # Device management app
├── assetprofile/        # Asset profile definitions
├── deviceprofile/       # Device profile definitions
├── manage.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit PRs.

---

## 🧾 License

This project is licensed under the MIT License.
