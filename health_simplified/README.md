# Health Simplified

Health Simplified is a simple command-line application to manage users and their food entries, including calorie tracking. It uses a SQLite database with SQLAlchemy ORM for data management.

## Features

- Manage users: create, update, delete, and list users.
- Manage food entries: add, update, delete, and list food entries with details such as food name, calories, and date.
- Simple CLI interface using Click.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd health_simplified
   ```

2. Create a virtual environment and activate it:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Database Setup

Run the database creation script to initialize the SQLite database:

```
python create_db.py
```

This will create the necessary tables in `health.db`.

## Usage

The application provides CLI commands to manage users and food entries.

### Main CLI

Run the main CLI:

```
python main.py
```

### User Commands

Manage users with the following commands:

- Create a user:
  ```
  python main.py user create
  ```

- Update a user:
  ```
  python main.py user update
  ```

- Delete a user:
  ```
  python main.py user delete
  ```

- List all users:
  ```
  python main.py user list
  ```

### Food Entry Commands

Manage food entries with the following commands:

- Add a food entry:
  ```
  python main.py food add
  ```

- Update a food entry:
  ```
  python main.py food update
  ```

- Delete a food entry:
  ```
  python main.py food delete
  ```

- List all food entries:
  ```
  python main.py food list
  ```

## Testing

To run tests (if any):

```
pytest
```

## License

This project is licensed under the MIT License.
