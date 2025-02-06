# 📊 Number Classification API  

A simple RESTful API that accepts a number as input and returns interesting mathematical properties along with a fun fact, powered by [Numbers API](http://numbersapi.com/#42).  

---

## 🚀 Features  
- Classifies numbers with properties such as **prime**, **perfect**, **Armstrong**, **odd/even**, and **digit sum**.  
- Provides a fun fact about the number using the Numbers API.  
- Handles **negative numbers** and validates inputs.  
- Returns JSON responses with appropriate status codes.  

---

## 🛠️ Technology Stack  
- **Language:** Python 🐍  
- **Framework:** Django + Django REST Framework (DRF)  
- **Deployment:** Publicly accessible endpoint (e.g., Vercel, Heroku, or Render)  
- **Others:** CORS handling, JSON responses  

---

## 📢 API Documentation  

### **Endpoint:**  
`GET <your-domain.com>/api/classify-number?number=<integer>`  

### **Response Formats:**  

#### ✅ **200 OK (Valid Number)**  
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

#### ❌ **400 Bad Request (Invalid Input)**  
```json
{
  "number": "alphabet",
  "error": true
}
```

---

## 💻 Installation and Setup  

### **Step 1: Clone the Repository**  
```bash
git clone https://github.com/chionz/HNGStage0.git"
cd <project directory>
```

### **Step 2: Set Up a Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
.\venv\Scripts\activate   # Windows
```

### **Step 3: Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **Step 4: Run Migrations**  
```bash
python manage.py migrate
```

### **Step 5: Start the Server**  
```bash
python manage.py runserver
```

---

## 🧪 Testing the API  

Once the server is running, you can test the API using:  
- **Postman** or **cURL**  
- Your browser: `http://127.0.0.1:8000/api/classify-number?number=371` 
 or `domain.com/api/classify-number?number=371` if deployed 

---

## 🌐 Deployment  

The API is hosted at: https://oderapg.pythonanywhere.com

---

## 📝 Project Structure  
```
number-classification-api/
    ├── manage.py          # Django project entry point
    ├── requirements.txt   # Project dependencies
    ├── api/               # API application containing views, serializers, and URLs
    ├── settings.py        # Django settings for the project
    └── README.md          # Documentation
```

---

## 🚦 Acceptance Criteria Checklist  

- [x] Accepts GET requests with a number parameter  
- [x] Returns JSON in the specified format  
- [x] Handles valid and invalid inputs properly  
- [x] Provides accurate HTTP status codes  
- [x] Hosted on a public endpoint  

---

## 🧑‍💻 Author  
**[Your Name](https://github.com/chionz)**  

---

## 📄 License  
This project is licensed under the MIT License.  

---

## 📚 Resources  
- [Numbers API](http://numbersapi.com/#42)  
- [Parity in Mathematics](https://en.wikipedia.org/wiki/Parity_(mathematics))  

---

Want me to customize this further? Just let me know! 😊
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



