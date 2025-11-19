from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login(request):
    if request.method != 'POST':
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=400)

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return JsonResponse({
                "status": True,
                "message": "Login successful!",
                "username": user.username,
            }, status=200)

        return JsonResponse({
            "status": False,
            "message": "Account disabled."
        }, status=401)

    return JsonResponse({
        "status": False,
        "message": "Incorrect username or password."
    }, status=401)

@csrf_exempt
def register(request):
    if request.method != 'POST':
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=400)

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({
            "status": False,
            "message": "Bad JSON."
        }, status=400)

    username = data.get("username")
    password1 = data.get("password1")
    password2 = data.get("password2")

    if password1 != password2:
        return JsonResponse({
            "status": False,
            "message": "Passwords do not match."
        }, status=400)

    if User.objects.filter(username=username).exists():
        return JsonResponse({
            "status": False,
            "message": "Username already exists."
        }, status=400)

    user = User.objects.create_user(username=username, password=password1)
    user.save()

    return JsonResponse({
        "status": "success",
        "message": "User created successfully!",
        "username": user.username,
    }, status=200)

@csrf_exempt
def logout(request):
    if not request.user.is_authenticated:
        return JsonResponse({
            "status": False,
            "message": "User is not logged in."
        }, status=401)

    username = request.user.username
    auth_logout(request)

    return JsonResponse({
        "status": True,
        "message": "Logged out successfully!",
        "username": username,
    }, status=200)
