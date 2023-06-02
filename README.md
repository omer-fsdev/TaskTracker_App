# TaskTracker App

TaskTracker App is a backend Django REST Framework project that allows to manage a todo list through a web interface.

## Features

- User registration and authentication
- Create, update, and delete tasks. Choose their priorities.
- Mark tasks as complete or incomplete
- API endpoints for CRUD operations on tasks

## Technologies Used

- Django
- Django REST Framework
- Python
- SQLite

## Installation

To run the Blog App locally, please follow these steps:

1. Clone the repository:

```
git clone https://github.com/omer-fsdev/TaskTracker_App.git
```

2. Navigate to the project directory:

```
cd TaskTracker_App
```

3. Create a virtual environment:

```
python3 -m venv env
```

4. Activate the virtual environment:

- For Windows:
  ```
  .\env\Scripts\activate
  ```
- For macOS and Linux:
  ```
  source env/bin/activate
  ```

5. Install the project dependencies:

```
pip install -r requirements.txt
```

6. Set up the database:

- Modify the database settings in the `settings.py` file to match your environment.
- Run the following command to migrate the database:
  ```
  python manage.py migrate
  ```

7. Start the development server:

```
python manage.py runserver
```

8. Access the application in your web browser at `http://localhost:8000`.

## API Documentation

For detailed API documentation, please refer to the `https://localhost:8000/api/schema/swagger-ui/`.
