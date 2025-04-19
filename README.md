# 🐍 FastAPI + PostgreSQL Application

A Python-based backend application using **FastAPI** as the REST API framework and **PostgreSQL** as the database engine. This app also supports **Excel file read/write**, **data validation**, and clean modular structure to scale efficiently.

## 🧰 Tech Stack & Tool Versions

| Tool         | Version      |
|--------------|--------------|
| Python       | 3.13.2       |
| pip          | 25.0.1       |
| PostgreSQL   | 17.4-1       |
| FastAPI      | ^0.110.0     |
| Uvicorn      | ^0.29.0      |
| SQLAlchemy   | ^2.0.28      |
| asyncpg      | ^0.29.0      |
| pandas       | ^2.2.2       |
| openpyxl     | ^3.1.2       |
| DBeaver (Optional GUI) | Latest |

---

## 🚀 Getting Started

### Prerequisites

Ensure the following are installed on your system:
- **Python 3.13.2** or higher
- **PostgreSQL 17.4-1**
- **Git**

---

### 1. **Clone the Repo**

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### 2. **Create a Virtual Environment (Recommended)**

```bash
py -m venv venv
venv\Scripts\activate   # On Windows
# Or
source venv/bin/activate  # On macOS/Linux
```

---

### 3. **Install Dependencies**

```bash
py -m pip install -r requirements.txt
```

---

### 4. **Set up PostgreSQL**

Ensure PostgreSQL is installed and running.  
You can use **DBeaver** or **pgAdmin** to manage your database.

#### 📦 Create Database

```sql
CREATE DATABASE mydatabase;
```

Replace `mydatabase` with your desired database name.

---

### 5. **Configure Environment Variables**

Create a `.env` file in the project root:

```
# .env
DATABASE_URL=postgresql+asyncpg://postgres:admin%40123@localhost:5432/mydatabase
```

Replace `admin%40123` with your actual PostgreSQL password (URL-encoded if it contains special characters).

---

### 6. **Run the Application**

```bash
py -m uvicorn main:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs) for interactive Swagger UI.

---

## 📂 Project Structure

```bash
.
├── app/
│   ├── main.py              # FastAPI app entrypoint
│   ├── models/              # SQLAlchemy models
│   ├── routes/              # API route handlers
│   ├── schemas/             # Pydantic schemas for request/response validation
│   ├── services/            # Business logic
│   ├── utils/               # Excel helpers, DB init, validators
├── .env                     # Environment config
├── requirements.txt         # Python dependencies
├── README.md                # This file
```

---

## 📤 Excel Integration

- Upload Excel → validate → store in DB
- Export DB data → downloadable Excel

> Uses `pandas` + `openpyxl` for full Excel read/write support.

---

## 🧪 Testing

To run tests, use the following command:

```bash
pytest
```

Ensure all dependencies are installed and the database is configured before running tests.

---

## 🤝 Contributing

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/awesome`)
3. Commit your changes (`git commit -m 'Add awesome feature'`)
4. Push to the branch (`git push origin feature/awesome`)
5. Open a pull request 🎉

---

## 🧠 Author

- Name: **Your Name**
- GitHub: [@your-username](https://github.com/your-username)
- Project Buddy: `ChatGPT` 🤖

---

## 🛡️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.