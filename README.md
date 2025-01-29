# Django Project

## Introduction

This is a Django-based project. Follow the steps below to set up the project on your local machine.

## Installation Guide

### 1. Clone the Repository

First, clone the repository from GitHub:

```sh
git clone https://github.com/chionz/HNGStage0.git
```

Navigate into the project directory:

```sh
cd <project-directory>
```

### 2. Set Up a Virtual Environment

Create a virtual environment to manage dependencies:

```sh
python -m venv .venv
```

### 3. Activate the Virtual Environment

Activate the virtual environment using the appropriate command for your operating system:

- **Windows (Command Prompt):**
  ```sh
  .venv\Scripts\activate
  ```
- **Windows (PowerShell):**
  ```sh
  .venv\Scripts\Activate.ps1
  ```
- **Linux/macOS:**
  ```sh
  source .venv/bin/activate
  ```

### 4. Install Dependencies

Once the virtual environment is activated, install the required dependencies:

```sh
pip install -r requirements.txt
```

### 5. Install Django (Optional)

If Django is not installed, you can install it manually:

```sh
pip install django
```

### 6. Run the Django Development Server

To start the Django development server, run:

```sh
python manage.py runserver
```

### 7. Access the Application

After running the server, open your browser and go to:

```
http://127.0.0.1:8000/
```

## Additional Notes

- Ensure you are inside the virtual environment whenever running Django commands.
- If you face any issues, ensure all dependencies are correctly installed.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

Happy coding! 🚀

