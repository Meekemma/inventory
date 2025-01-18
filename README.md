# Inventory Management System

## Overview

The **Inventory Management System** is a web application built with **Django** and **Django REST Framework**. This system provides user authentication, inventory management, order tracking, and reporting functionalities for both admins and regular users. Admins can manage products, orders, and view reports, while regular users can create orders and view available products.

## Features

### User Authentication
- User registration, login, and logout.
- Role-based access control (Admin and Regular User).

### Inventory Management
- Admins can add, update, and delete products.
- Each product includes name, description, quantity, and price.
- Regular users can view product lists but cannot modify them.

### Order Management
- Users can create orders with products and quantities.
- Orders include status tracking (pending, completed, or canceled).
- Admins can update order statuses.

### Reporting
- Endpoint to list low-stock products (quantity < 10).
- Endpoint to generate sales reports (daily, weekly, monthly).

## Technologies Used

- **Python**
- **Django**
- **Django REST Framework**
- **SQLite**
- **And more...**

## Installation

Follow these steps to set up and run the project locally:

### 1. Clone the repository
Clone this repository to your local machine:

```bash
git clone https://github.com/Meekemma/inventory.git
cd inventory
```

### 2. Set up a virtual environment
Create and activate a virtual environment to isolate project dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
Install the required packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Generate Django Secret Key
Use OpenSSL to generate a secure random secret key for your project:

```bash
openssl rand -base64 32
```

Copy the generated key and save it in a `.env` file located in the root of your project:

```bash
DJANGO_SECRET_KEY='your-generated-secret-key'
```

### 5. Apply database migrations
Run database migrations to set up the necessary tables:

```bash
python manage.py migrate
```

### 6. Start the development server
Run the development server to view the application:

```bash
python manage.py runserver
```

Now, you can access the application at `http://127.0.0.1:8000/`.

## API Endpoints

### Base App
- `POST /base/registration/` - User registration.
- `POST /base/login/` - User login.
- `POST /base/login/refresh/` - Refresh JWT tokens.
- `POST /base/logout/` - User logout.

### Inventory Management App
- `GET /inventory_management/products/` - View product list (Regular Users).
- `POST /inventory_management/products/create/` - Add a new product (Admins).
- `PUT /inventory_management/products/update/<id>/` - Update a product (Admins).
- `DELETE /inventory_management/products/delete/<id>/` - Delete a product (Admins).
- `GET /inventory_management/products/<id>/` - View product details (Regular Users).

### Order App
- `POST /order/create-order/` - Create a new order.
- `GET /order/track_status/` - Track order status.
- `PATCH /order/status_update/<id>/` - Update order status (Admins).

### Report App
- `GET /report/stock_report/` - Low-stock products.
- `GET /report/sales_report/` - Sales reports by day/week/month.

## Testing

To run tests, use the following command:

```bash
pytest
```

The tests cover the following:
- User authentication and authorization.
- Inventory management functionalities.
- Order creation and status updates.
- Reporting endpoints.

## Error Handling

The application provides appropriate error responses:
- **400 Bad Request**: For invalid input data.
- **401 Unauthorized**: For unauthenticated access.
- **403 Forbidden**: For unauthorized access.
- **404 Not Found**: For non-existing resources.
- **500 Internal Server Error**: For unexpected server errors.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

Created by [Emmanuel (meekemma)](https://github.com/Meekemma) - Feel free to reach out!

