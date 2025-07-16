# 🍭 Incubyte Sweet Shop Management System

A **Test-Driven Development (TDD)** focused sweet shop inventory management system built with FastAPI. This project demonstrates clean code practices, comprehensive testing, and modern web development techniques.

## 🎯 TDD Focus & Development Approach

This project follows **Test-Driven Development (TDD)** methodology:

- ✅ **Red-Green-Refactor Cycle**: Tests written before implementation
- ✅ **Clean Architecture**: Separation of concerns with testable components
- ✅ **Continuous Testing**: Easy test execution and validation

## ✨ Features

- **Inventory Management**: Add, view, delete, and manage sweet items
- **Stock Control**: Purchase sweets and restock inventory with validation
- **Search & Sort**: Filter by name, category, price; sort by various criteria
- **RESTful API**: FastAPI with automatic documentation
- **Responsive UI**: Bootstrap-based web interface

## 🛠 Tech Stack

- **Backend**: FastAPI (Python 3.11), Uvicorn
- **Frontend**: HTML5, Bootstrap 5, Jinja2
- **Testing**: unittest, TDD methodology
- **Containerization**: Docker


## 🧪 Testing (TDD Focus)

### Run Tests
```bash
cd sweet_shop

# Run all tests
python -m unittest discover tests/ -v

# Run specific test class
python -m unittest tests.test_shop.TestSweetShop_AddSweet -v
```

## 🚀 Quick Start

### Method 1: Local Setup

```bash
# Clone and setup
git clone https://github.com/MercyShark/Incubyte-Assignment-Sweet-Shop-Management-System.git . 

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies and run
pip install -r requirements.txt
cd sweet_shop
python main.py
```

**Access**: http://localhost:8000

### Method 2: Docker Setup

```bash
# Build and run
git clone https://github.com/MercyShark/Incubyte-Assignment-Sweet-Shop-Management-System.git . 

docker build -t sweet-shop .
docker run -p 8000:8000 sweet-shop
```

**Access**: http://localhost:8000



![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)