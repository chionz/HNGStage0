from datetime import datetime, timezone
from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.http import require_GET

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
