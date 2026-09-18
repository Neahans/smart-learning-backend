<div align="center">

# 🐍 Smart Learning Backend

<img
src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=30&pause=900&color=866BE8&center=true&vCenter=true&width=900&lines=Welcome+to+Smart+Learning+Backend+%F0%9F%92%9C;Django+%E2%80%A2+REST+API+%E2%80%A2+Database+%F0%9F%90%8D;Powering+the+Smart+Learning+Platform+%E2%9C%A8;Learn+%E2%80%A2+Build+%E2%80%A2+Grow+%F0%9F%8C%B8"
alt="Typing Animation"
/>

<br>

<img
src="https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif"
width="350"
alt="Coding GIF"
/>

<br><br>

<img src="https://img.shields.io/badge/Python-Backend-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Django-Framework-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
<img src="https://img.shields.io/badge/DRF-REST%20API-866BE8?style=for-the-badge" alt="Django REST Framework">
<img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
<img src="https://img.shields.io/badge/CORS-Enabled-AC86E9?style=for-the-badge" alt="CORS">

<br><br>

<img
src="https://capsule-render.vercel.app/api?type=waving&color=0:866BE8,50:AC86E9,100:D95DF8&height=180&section=header&text=SMART%20LEARNING%20BACKEND&fontSize=38&fontColor=ffffff&animation=fadeIn&fontAlignY=55"
width="100%"
alt="Smart Learning Backend Header"
/>

</div>

---

## 🌸 About Smart Learning Backend

The **Smart Learning Backend** is a Django-based backend for the Smart Learning Management System.

It provides the REST API layer used by the React frontend and manages learning-related data such as:

* 🎓 Students
* 👩🏻‍🏫 Mentors
* 📚 Courses
* 🧩 Modules
* 📝 Notes
* 🔓 Module Unlock Requests

The backend is being developed using **Django REST Framework (DRF)** to provide API-based communication between the frontend and backend.

---

## ✨ Main Features

<div align="center">

| Feature | Status |
| :----------------------- | :----: |
| 🐍 Django Project | ✅ |
| ⚙️ Django REST Framework | ✅ |
| 📚 Course Model | ✅ |
| 🔗 Course API | ✅ |
| 🔄 ViewSets | ✅ |
| 🚦 API Routers | ✅ |
| 🌐 CORS Configuration | ✅ |
| 📡 React API Connection | ✅ |
| 🧩 Module API | 🔄 |
| 📝 Notes API | ⬜ |
| 🔓 Unlock Request API | ⬜ |
| 🔐 JWT Authentication | ⬜ |

</div>

---

## 🏗️ Backend Architecture

<div align="center">

```text
                  ⚛️ REACT FRONTEND
                          │
                          │ Axios
                          ▼
                   🔗 REST API
                          │
                          ▼
                   🐍 DJANGO
                          │
                ┌─────────┴─────────┐
                │                   │
                ▼                   ▼
        Django REST Framework    Models
                │                   │
                └─────────┬─────────┘
                          │
                          ▼
                    🗄️ DATABASE
```
</div>

📚 Current API
Courses API

The current backend provides a Courses API through Django REST Framework.

Endpoint
http://127.0.0.1:8000/api/courses/
Available Operations
Method	Endpoint	Description
GET	/api/courses/	List all courses
POST	/api/courses/	Create a course
GET	/api/courses/<id>/	Retrieve a course
PUT	/api/courses/<id>/	Update a course
PATCH	/api/courses/<id>/	Partially update a course
DELETE	/api/courses/<id>/	Delete a course
🧩 Course Model

The current Course model contains:

title
description
instructor
category
level
modules_count
students_count
progress
image
🛠️ Tech Stack
<div align="center">
Backend
<img src="https://skillicons.dev/icons?i=python,django,sqlite" alt="Backend Technologies">

<br><br>

Development Tools
<img src="https://skillicons.dev/icons?i=git,github,vscode" alt="Development Tools"> </div>
Technologies Used
🐍 Python
🌿 Django
🔗 Django REST Framework
🗄️ SQLite
🌐 django-cors-headers
🔎 django-filter
📡 REST APIs
🏗️ Project Structure
smart_learning/
│
├── learning/
│   ├── migrations/
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── smart_learning/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
⚙️ Setup
1️⃣ Clone the Repository
git clone https://github.com/Neahans/smart-learning-backend.git
2️⃣ Open the Project
cd smart-learning-backend
3️⃣ Create a Virtual Environment
python -m venv venv
4️⃣ Activate the Virtual Environment
Windows PowerShell
.\venv\Scripts\Activate.ps1
5️⃣ Install Dependencies
pip install -r requirements.txt
6️⃣ Apply Migrations
python manage.py migrate
7️⃣ Start the Development Server
python manage.py runserver

The backend will run at:

http://127.0.0.1:8000/
📡 API Connection

The React frontend connects to the Django API using Axios.

Example Frontend Configuration
import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
});

export default api;
Example Request
const response = await api.get("courses/");
🌐 CORS

CORS is configured so that the React development server can communicate with the Django backend.

Development URLs

React Frontend

http://localhost:3000

Django Backend

http://127.0.0.1:8000
🗄️ Database

The project currently uses SQLite for development.

Database File
db.sqlite3

The local database is excluded from Git using .gitignore.

🌱 Development Status
Completed
✅ Django project setup
✅ Learning app setup
✅ Django REST Framework setup
✅ CORS configuration
✅ Course model
✅ Course serializer
✅ Course ViewSet
✅ API router
✅ Course CRUD API
✅ Sample course data
✅ React → Django Courses connection
In Progress
🔄 Module API
Planned
⬜ Notes API
⬜ Unlock Request API
⬜ JWT Authentication
⬜ Role-based API permissions
⬜ API filtering
⬜ API pagination
🗺️ Future Backend Work
🔐 JWT Authentication
👥 User & Role Management
📚 Course API
🧩 Module API
📝 Notes API
🔓 Unlock Request API
🔎 Search & Filtering
📄 Pagination
🛡️ Role-based Permissions
📊 Dashboard Analytics API
⚛️ Frontend

The React frontend for this project is maintained separately.

<div align="center"> <a href="https://github.com/Neahans/smart-learning-frontend">

<img src="https://img.shields.io/badge/⚛️%20Smart%20Learning%20Frontend-View%20Repository-866BE8?style=for-the-badge" alt="Frontend Repository" />

</a>

<br><br>

🔗 Smart Learning Frontend Repository

</div>
🔗 Project Repositories
<div align="center">
🐍 Backend

🔗 smart-learning-backend

<br><br>

⚛️ Frontend

🔗 smart-learning-frontend

</div>
💜 Full-Stack Connection
<div align="center">
          ⚛️ REACT FRONTEND
                 │
                 │ Axios
                 ▼
          🔗 DJANGO REST API
                 │
                 ▼
             🐍 DJANGO
                 │
                 ▼
            🗄️ SQLITE DB
</div>
<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=22&pause=1000&color=866BE8&center=true&vCenter=true&width=700&lines=Learn+%F0%9F%8C%B8;Build+%F0%9F%92%9C;Connect+%E2%9C%A8;Grow+%F0%9F%9A%80" alt="Footer Animation" />

<br><br>

🌷 Made with Django, code, and a little purple magic. 💜

<br><br>

⭐ Thanks for visiting Smart Learning Backend!

<br><br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:866BE8,50:AC86E9,100:D95DF8&height=120&section=footer&animation=fadeIn" width="100%" alt="Footer" />

</div> 
