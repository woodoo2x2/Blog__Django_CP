



## It's my Blog Django Project Readme

# Project Title

It's my first combat Django Application.

## Table of Contents

- [Technologies](#technologies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [Testing](#testing)
- [Development](#development)


## Technologies

- Python 3.10
- Django 5
- PostgreSQL (need to realise)
- Docker (need to realise)
- Redis (need to realise)
- DRF  (need to realise)

## Installation

1. Clone the repository
    ```sh
    git clone https://github.com/woodoo2x2/Blog__Django_CP.git
    cd project-name
    ```

2. Create and activate a virtual environment
    ```sh
    python -m venv venv
    source venv/bin/activate  # use `venv\Scripts\activate` for Windows
    ```

3. Install dependencies
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file and configure environment variables
    ```env
    DEBUG=True
    SECRET_KEY='your-secret-key'
    DATABASE_URL='your-database-url'
    ```

## Configuration

1. Apply database migrations
    ```sh
    python manage.py migrate
    ```

2. Create a superuser
    ```sh
    python manage.py createsuperuser
    ```

3. Collect static files
    ```sh
    python manage.py collectstatic
    ```

## Running the Project

1. Start the development server
    ```sh
    python manage.py runserver
    ```

2. Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Testing

1. Run tests
    ```sh
    python manage.py test
    ```

## Development

### Project Structure

A brief description of the project structure and main directories.

- `Blog__Django_CP/` - root directory of the project
- `Blog__Django_CP//settings/` - Django settings
- `Blog__Django_CP//urls.py` - routing
- `blog/` - blog application
- `accounts/` - acconts application

### Common Commands

- Create an application
    ```sh
    python manage.py startapp app_name
    ```

- Apply migrations
    ```sh
    python manage.py migrate
    ```

- Create migrations
    ```sh
    python manage.py makemigrations
    ```




### Learning goals
- Learn To work with ClassBasedViews
- Special adjustment for admin panel
- Testing and using django-debug-toolbar and check (select_related())
- Connect Bootstrap
- Creating Profiles, realise Login/Logout system
- Working with mixins and create custom one
- Using common uses ViewBasedClasses
- Using mptt, create Comment Tree (Using JavaScript) and Category Tree
- Using and create custom middleware
