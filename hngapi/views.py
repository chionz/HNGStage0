from datetime import datetime, timezone
from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.http import require_GET

import math
import requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@require_GET
def stage0(request):
    email = "chideraprince9@gmail.com"
    date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    github = "https://github.com/chionz/HNGStage0"

    response ={
        "email": email,
        "current_datetime": date,
        "github_url": github
    }

    return JsonResponse(response)




@require_GET
def classify_number(request):
    tempnumber = request.GET.get('number')
    
    # Check if the input is a valid integer (including negative numbers)
    if not tempnumber or not tempnumber.lstrip('-').isdigit():
        return JsonResponse({
            "number": "alphabet",
            "error": True
        }, status=400)

    number = int(tempnumber)  # Keep the number as it is (including negative sign)
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_perfect(n):
        if n < 1:
            return False  # No negative perfect numbers
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n

    def is_armstrong(n):
        digits = [int(d) for d in str(abs(n))]  # Use absolute value for Armstrong check
        return sum([d ** len(digits) for d in digits]) == abs(n)

    digit_sum = sum(int(d) for d in str(abs(number)))  # Sum digits of the absolute value

    # Get a fun fact about the number
    try:
        response = requests.get(f"http://numbersapi.com/{tempnumber}")
        fun_fact = response.text if response.status_code == 200 else "No fun fact available."
    except requests.RequestException:
        fun_fact = "Fun fact not available due to a connection error."

    # Prepare the result
    result = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": [
            "armstrong" if is_armstrong(number) else None,
            "odd" if number % 2 != 0 else "even"
        ],
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }

    # Remove None values from properties
    result["properties"] = [prop for prop in result["properties"] if prop]

    return JsonResponse(result)
