# Student Loan System

A student loan application and management system developed using Python, Flask, HTML, CSS, JavaScript, and MongoDB.

The system allows students to submit loan applications and provides a dashboard for viewing submitted applications and monitoring loan requests.

## Features

- Student loan application form
- Loan application processing
- View submitted applications
- Dashboard with application statistics
- MongoDB database for storing application data
- Automatic loan approval decision
- Simple and responsive user interface

## Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- MongoDB
- Git and GitHub

## System Flow

```text
Student
   ↓
Loan Application Form
   ↓
Flask Backend
   ↓
Loan Processing
   ↓
MongoDB Database
   ↓
Application Result
```

## Project Structure

```text
student-loan-system/
│
├── app.py
├── loan.db
├── requirements.txt
├── README.md
├── LICENSE
│
├── static/
│   ├── script.js
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── applications.html
│   └── dashboard.html
│
└── screenshots/
    ├── home.png
    ├── applications.png
    └── dashboard.png
```

### File Description

| File / Folder | Description |
|---|---|
| `app.py` | Main Flask application |
| `requirements.txt` | Python dependencies |
| `static/` | CSS and JavaScript files |
| `templates/` | HTML pages |
| `screenshots/` | Screenshots of the application |
| `README.md` | Project documentation |
| `LICENSE` | Project license |

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/jupeang/student-loan-system.git
```

### 2. Open the project

```bash
cd student-loan-system
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

On Windows:

```bash
venv\Scripts\activate
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

### 6. Start MongoDB

Make sure MongoDB is installed and running on your computer.

The application uses:

```text
mongodb://localhost:27017/
```

### 7. Run the application

```bash
python app.py
```

### 8. Open the application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Screenshots

### Home / Loan Application

![Home Page](screenshots/home.png)

### Applications Page

![Applications Page](screenshots/applications.png)

### Dashboard

![Dashboard](screenshots/dashboard.png)

## Future Improvements

Possible future improvements include:

- Student and administrator login
- Role-based access control
- Email notifications
- Advanced application search and filtering
- Improved loan analytics
- Mobile application support
- Cloud deployment
- Machine learning-based loan prediction

## Author

**Justus Peter**

Bachelor of Computer Science  
South Eastern Kenya University

**GitHub:** https://github.com/jupeang  
**Portfolio:** https://jupeang.github.io/my-portfolio/  
**Email:** justusmalombep@gmail.com
