# Django Newspaper App

A newspaper web application built with Django using only class-based views. Users can register, post articles, and comment.

## Features

- User registration and authentication
- Create, edit, and delete articles
- Add comments to articles
- Clean code using Django class-based views

## Getting Started

1. **Clone the repository:**
   ```
   git clone https://github.com/Fiow00/django_for_beginners.git
   cd django_for_beginners
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Apply migrations:**
   ```
   python manage.py migrate
   ```

4. **Create a superuser (optional):**
   ```
   python manage.py createsuperuser
   ```

5. **Run the development server:**
   ```
   python manage.py runserver
   ```

6. **Open your browser and go to:**
   ```
   http://127.0.0.1:8000/
   ```

## Project Structure

- `accounts/` – User authentication and registration
- `newspaper/` – Article and comment management
