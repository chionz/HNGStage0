# HNG12 Stage 1 API - **Number Classification API**

An API that classifies numbers based on mathematical properties and provides a fun fact about them.

## **Features**

- Determines if a number is **prime**, **perfect**, or an **Armstrong number**.
- Classifies numbers as **odd** or **even**.
- Computes the **sum of the digits** of a number.
- Fetches a **fun fact** from the [Numbers API](http://numbersapi.com/).
- Returns structured **JSON responses**.

## **Live Demo**

🚀 **Base URL:**

```
https://oderapg.pythonanywhere.com
```

## **API Documentation**

### **Endpoint:**

```
GET /api/classify-number?number={number}
```

### **Example Request**

```bash
curl -X GET "https://oderapg.pythonanywhere.com/api/classify-number?number=371"
```

### **Successful Response (200 OK)**

```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### **Error Response (400 Bad Request)**

```json
{
  "number": "alphabet",
  "error": true
}
```
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

## Deployment

This API is deployed on **Railway**. Any changes pushed to the main branch automatically redeploy the project.



## Additional Note

- API responds in **<500ms**.
- Handles **CORS** for cross-origin requests.
- Supports **only integer inputs**.
- Ensure you are inside the virtual environment whenever running Django commands.
- If you face any issues, ensure all dependencies are correctly installed.
- Hey, if you want to hire a reliable python developer go to [HNG Developer](https://hng.tech/hire/python-developers)

## License

This project is open-source and available under the [MIT License](LICENSE).

---



