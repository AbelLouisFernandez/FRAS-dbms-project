# Ambulance Booking System

## Setup Instructions

Follow the steps below to set up and run the project on your local machine.

### 1. Create a MySQL Database
First, create a MySQL database named `ambulance` using the MySQL command line:
```sql
CREATE DATABASE ambulance;
```

### 2. Set Up the Project in VS Code
- Open VS Code and navigate to your project folder.

### 3. Create and Activate a Virtual Environment
Run the following commands in your terminal:

#### Create a virtual environment:
```sh
python -m venv virtual_environment_name
```

#### Activate the virtual environment:
- **Windows:**
  ```sh
  virtual_environment_name\Scripts\activate.bat
  ```
- **Linux/Mac:**
  ```sh
  source virtual_environment_name/bin/activate
  ```

### 4. Install Required Packages
Run the following command to install dependencies:
```sh
pip install -r requirements.txt
```

### 5. Run the Django Server
Start the development server with:
```sh
python manage.py runserver
```

Your Django server should now be running, and you can access the application in your web browser.