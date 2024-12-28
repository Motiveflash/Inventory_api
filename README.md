# Inventory Management API

A robust Inventory Management API built with Django and Django REST Framework (DRF) that allows users to manage inventory items, track inventory changes, and handle user authentication. The API is designed to simulate real-world inventory management for a store, providing essential CRUD operations, user management, and secure authentication.

---

## Features

- **User Management:**
  - Register, login, and manage users.
  - Token-based authentication using JWT.
  - Role-based access control.

- **Inventory Item Management:**
  - Create, read, update, and delete inventory items.
  - Track essential attributes like name, description, quantity, price, category, and timestamps.

- **Inventory Change Log:**
  - Log and track changes to inventory items (e.g., restocking or sales).
  - View the change history of inventory items.

- **Advanced Features:**
  - Pagination and sorting of inventory items.
  - Filters for categories, price range, and low stock.
  - Optional features like low-stock alerts, supplier management, and multi-store support.

- **Deployment-Ready:**
  - Deployed on Heroku or PythonAnywhere.
  - Secure and scalable.

---

## Tech Stack

- **Backend Framework:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** JWT (JSON Web Tokens)
- **Deployment:** Heroku or PythonAnywhere
- **Environment Variables Management:** `python-dotenv`

---

## Prerequisites

- Python 3.10+
- PostgreSQL database
- Pipenv or pip for managing dependencies

---

## Installation and Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/inventory-management-api.git
   cd inventory-management-api
