# 🛒 Online Store Management System (CLI Project)

A professional Python Command-Line Interface (CLI) application that simulates a real-world online shopping system.  
This project was built to practice **Object-Oriented Programming, file handling, and software architecture fundamentals** in Python.

---

## 👨‍💻 Developer

**Name:** Mahdi Ali Iltireh  
**GitHub:** [MahdiDevSo](https://github.com/MahdiDevSo)

---

## 📌 Project Overview

The **Online Store Management System** is a CLI-based application that allows users to manage products, add items to a shopping cart, and complete a checkout process.

It simulates the core structure of a real e-commerce system, including:

- Product management
- Inventory control
- Shopping cart system
- Order checkout process
- File-based data storage


---

## 🎯 Key Objectives

- Build a real-world CLI application
- Apply Object-Oriented Programming (OOP)
- Practice modular project structure
- Handle file storage and persistence
- Implement error handling using `try/except`
- Simulate real business logic (store + cart + checkout)

---

## 🧠 Concepts Used

| Concept | Description |
|----------|-------------|
| Variables | Store product data |
| Conditions | Menu and logic control |
| Loops | Repeated menu interaction |
| Functions | Reusable code blocks |
| Lists | Store products and cart items |
| Classes | Product, Cart, Store logic |
| `@dataclass` | Clean data modeling |
| `__str__` | Readable object output |
| Composition | Store contains products/cart |
| File Handling | Save/load data |
| Exception Handling | Prevent runtime crashes |

---

## 📁 Project Structure

```bash
Final_project_Online_Store_System/
│
├── main.py   
├── README.md               
│
├── models/
│   └── store.py           
│
├── utils/
│   └── storage.py         
│
└── data/
    └── products.txt       
```

# 🏗️ System Architecture

```text
User
  ↓
CLI Interface (main.py)
  ↓
Business Logic (store.py)
  ↓
Storage Layer (storage.py)
  ↓
products.txt
```
---

# ⚙️ Core Features

##  Product Management

The system allows users to:

- Add products
- View all products
- Manage stock quantities

---

##  Shopping Cart System

Users can:

- Add items to cart
- Increase quantities
- View cart contents
- Calculate total price

---

##  Inventory Management

The application automatically:

- Reduces stock after purchase
- Prevents invalid purchases
- Tracks available inventory

---

##  Persistent Data Storage

The system stores product information inside a UTF-8 text file.

- Saving data permanently
- Loading data automatically
- Simulating a lightweight database

---

##  Error Handling

The application uses `try/except` blocks to:

- Handle invalid numeric input
- Prevent crashes
- Improve user experience

---

# 🧩 Main Classes

## 📦 Product Class

Represents a store item.

### Attributes

- `id`
- `name`
- `price`
- `stock`

---

## 🛒 CartItem Class

Represents:

- A product
- Quantity selected by customer

---

## 🏪 Store Class

Controls:

- Product management
- Cart operations
- Checkout process
- Inventory updates

---

# 💾 Data Storage Format

The project stores data in:

```text
data/products.txt
```

### Example

```text
# id|name|price|stock
1|Laptop|800|10
2|Mouse|20|50
3|Keyboard|45|30
```

---

# 🖥️ Application Menu

```text
===== ONLINE STORE =====

1. Add product
2. List products
3. Add to cart
4. View cart
5. Checkout
6. Save
7. Quit
```

---

# 🔄 System Workflow

```text
Start Program
    ↓
Load Products
    ↓
Display Menu
    ↓
User Selects Action
    ↓
Process Operation
    ↓
Save Data
    ↓
Exit Program
```

---

# 🧪 Example Product Object

```python
Product(
    id=1,
    name="Laptop",
    price=800,
    stock=10
)
```

---


# ⭐ Final Note

This project is an important step from:

```text
Learning Python
        ↓
Building Real Applications
        ↓
Thinking Like a Software Developer
```