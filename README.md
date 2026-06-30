# 🍽️ TasteBite Restaurant Management System

A role-based Restaurant Management System developed using **Python**, **Django**, **HTML**, **CSS**, **JavaScript**, **Bootstrap**,
and **SQLite**. The system streamlines restaurant operations by providing dedicated dashboards for Customers, Waiters, and Chefs, 
ensuring an efficient order management workflow from table booking to bill generation.

---

## 📌 Project Overview

TasteBite Restaurant Management System is a full-stack Django web application designed to automate restaurant operations. Customers
can reserve tables, browse the menu, place food orders, and track their order status. Waiters manage customer orders, while chefs
handle kitchen preparation through dedicated dashboards.

The application follows a complete restaurant workflow and provides an intuitive user experience with responsive design and 
interactive analytics.

---

## 🚀 Features

### 👤 Customer Module

- User Registration & Login
- Role-Based Authentication
- Restaurant Table Booking
- Browse Food Menu
- Add Food to Cart
- Update Cart Quantity
- Remove Cart Items
- Place Order
- Order Success Page
- View Bill

---

### 👨‍🍳 Chef Dashboard

- View Confirmed Orders
- Start Preparing Orders
- Mark Orders as Ready
- Kitchen Order Queue
- Order Status Management

---

### 👨‍💼 Waiter Dashboard

- View Customer Orders
- Confirm Orders
- Serve Ready Orders
- Generate Customer Bill
- Order Status Analysis (Bar Chart)
- Dashboard Statistics

---

### 📄 Billing System

- Generate Customer Bill
- Automatic GST Calculation
- Grand Total Calculation
- Print Bill
- Professional Invoice Layout

---

### 📊 Dashboard Analytics

- Total Orders
- Pending Orders
- Confirmed Orders
- Preparing Orders
- Ready Orders
- Completed Orders
- Interactive Order Status Bar Chart

---

### 📱 Responsive Design

- Desktop Friendly
- Tablet Responsive
- Mobile Responsive

---

## 🔄 Restaurant Workflow

```
Customer
    │
    ▼
Select Table
    │
    ▼
Browse Menu
    │
    ▼
Add Food to Cart
    │
    ▼
Place Order
    │
    ▼
Waiter Dashboard
(Confirm Order)
    │
    ▼
Chef Dashboard
(Start Preparing)
    │
    ▼
Mark Ready
    │
    ▼
Waiter Dashboard
(Serve Food)
    │
    ▼
Generate Bill
    │
    ▼
Customer Bill
```

---

## 🛠️ Tech Stack

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Chart.js

### Backend

- Python
- Django

### Database

- SQLite

### Deployment

- Render

### Version Control

- Git
- GitHub

---

## 📂 Project Structure

```
Tastebite-Restaurant-Website
│
├── restapp/
├── restaurant/
├── media/
├── templates/
├── manage.py
├── requirements.txt
├── Procfile
├── runtime.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Mathan495/Tastebite-Restaurant-Website.git
```

### Go to Project

```bash
cd Tastebite-Restaurant-Website
```

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Environment

Windows

```bash
env\Scripts\activate
```

Linux / Mac

```bash
source env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Start Server

```bash
python manage.py runserver
```

---

## 🔑 User Roles

### Customer

- Book Table
- Browse Menu
- Add to Cart
- Place Order
- View Bill

---

### Waiter

- Confirm Orders
- Serve Food
- Generate Bill
- Monitor Orders

---

### Chef

- View Confirmed Orders
- Prepare Food
- Mark Orders Ready

---

## 📈 Order Status Flow

```
Pending
   │
   ▼
Confirmed
   │
   ▼
Preparing
   │
   ▼
Ready
   │
   ▼
Completed
   │
   ▼
Bill Generated
```

## 🔮 Future Enhancements

- Online Payment Integration
- QR Code Menu
- Customer Order Tracking
- Email Notifications
- SMS Notifications
- AI Food Recommendation
- AI Customer Chatbot
- Online Table Reservation
- Cloudinary Image Storage
- PostgreSQL Database
- Docker Deployment

---

## 🎯 Learning Outcomes

- Django Authentication
- Role-Based Access Control
- CRUD Operations
- Database Relationships
- Order Management Workflow
- Dashboard Analytics
- Responsive Web Design
- Bill Generation System
- Deployment on Render

---

## 📧 Contact

**Mathan Kumar G**

💻 GitHub: https://github.com/Mathan495

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

---

## 📄 License

This project is developed for educational purposes and portfolio demonstration.
