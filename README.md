# Customer Registration API

## Overview

This project implements a RESTful API for managing customer personal and employment details using Django and Django REST Framework. It provides CRUD operations for both personal and employment records.

## Features

- **CRUD Operations:** Create, Read, Update, and Delete operations for both Personal Details and Employment Details.
- **Validations:** Ensures data integrity with specific validations for fields like email and phone number.
- **Swagger UI:** Interactive API documentation for easy exploration and testing of endpoints.

## Project Setup

### Environment

- **Python Environment:** `myenv`

### Requirements

- Python 3.x
- Django
- Django REST Framework
- drf-spectacular (for Swagger UI)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/anshaduk/customer-registration.git
   cd customer-registration

2. **Setup Virtual Environment:**
   myenv\Scripts\activate

3.  **Install dependencies:**
    pip install -r requirements.txt

4.  **Migrate the database:**
    python manage.py migrate

5.  **Run the server**
    python manage.py runserver


## API Endpoints

### Personal Details
1. List/Add Personal Details: GET/POST /api/personal/
2. Retrieve/Update/Delete Personal Detail: GET/PUT/DELETE /api/personal/<id>/

### Employment Details
1. List/Add Employment Details: GET/POST /api/employment/
2. Retrieve/Update/Delete Employment Detail: GET/PUT/DELETE /api/employment/<id>/

### Swagger Documentation
Access the Swagger UI at: http://127.0.0.1:8000/api/schema/swagger-ui/
