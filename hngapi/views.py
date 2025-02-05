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
    number = request.GET.get('number')
    
    if not number or not number.isdigit():
        return JsonResponse({"error": "Please provide a valid number."}, status=400)

    number = int(number)

   
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

   
    def is_perfect(n):
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n

 
    def is_armstrong(n):
        digits = [int(d) for d in str(n)]
        return sum([d ** len(digits) for d in digits]) == n

  
    digit_sum = sum(int(d) for d in str(number))

   
    response = requests.get(f"http://numbersapi.com/{number}")
    fun_fact = response.text if response.status_code == 200 else "No fun fact available."

   
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

   
    result["properties"] = [prop for prop in result["properties"] if prop]

    return JsonResponse(result)
