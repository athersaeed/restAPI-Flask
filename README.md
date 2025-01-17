# Flask REST API with SQLAlchemy and Flask-RESTful

A simple **REST API** built with **Flask**, **SQLAlchemy**, and **Flask-RESTful** that demonstrates basic **CRUD** operations for a `UserModel` resource (Create, Read, Update, and Delete—although this example covers Create and Read explicitly).

## Features

- **SQLite** database for easy local development.
- **SQLAlchemy** ORM for interacting with the database.
- **Flask-RESTful** for creating resource-based endpoints.
- **Request parser** validation to ensure request data is valid.

## Requirements

- **Python 3.7+**  
- **pip** or **pipenv/poetry** (optional but recommended)

## Getting Started

1. **Clone the repository** (or download the `.zip`):
    ```bash
    git clone https://github.com/YourUsername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a virtual environment** (recommended):
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On macOS/Linux
    .venv\Scripts\activate     # On Windows
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
   > If you don't have a `requirements.txt` yet, you can create one by installing the needed packages (`Flask`, `Flask-SQLAlchemy`, `Flask-RESTful`) and then running `pip freeze > requirements.txt`.

4. **Initialize the Database**  
   We need to create our database tables before running the application. You can do this by running a small snippet of code or by updating the code to include `db.create_all()`. For a quick approach, place the following snippet right before `if __name__ == '__main__':`:
   ```python
   with app.app_context():
       db.create_all()
   ```

5. **Run the Application**
   ```pythongit
   python api.py
   ```

## Project Structure
   ```bash
   .
   ├── api.py               # Main Flask application and API routes
   ├── instance # Contains the SQLite database 
   │ └── database.db # SQLite database (generated once the createdb.py runs
   ├── requirements.txt     # Python dependencies (optional)
   └── README.md            # Project documentation
   ```

## Endpoints

1.  `GET /api/users/`
   - **Description:** Fetches all users from the database.
   - **Response: (JSON):**
   ```json
  {
    "id": 1,
    "name": "Shane",
    "email": "shane@example.com"
    }
  ```
2.  `POST /api/users/`
   - **Description:** Creates all users from the database.
   - **Response: (JSON):**
   ```json
  {
    "id": 1,
    "name": "Shane",
    "email": "shane@example.com"
    }
  ```
3.  `GET /api/users/<int>:ID`
   - **Description:** Fetches a user from the database using the ID.
   - **Response: (JSON):**
   ```json
  {
    "id": 1,
    "name": "Shane",
    "email": "shane@example.com"
    }
  ```
4.  `PATCH /api/users/<int>:ID`
   - **Description:** Updates a user from the database using the ID and returns the updated user.
   - **Response: (JSON):**
   ```json
  {
    "id": 1,
    "name": "Shane",
    "email": "shane@example.com"
    }
  ```
5.  `DELETE /api/users/<int>:ID`
   - **Description:** Deletes a user from the database using the ID and returns the remaining users.
   - **Response: (JSON):**
   ```json
  {
    "id": 1,
    "name": "Shane",
    "email": "shane@example.com"
    }
  ```