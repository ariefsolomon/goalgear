from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags


# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)
    context = {
        'app_name': 'GoalGear',
        'student_name': request.user.username,
        'student_class': 'PBP E',
        'product_list' : product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }
    return render(request, 'main.html', context)

def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect("main:show_main")
    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {'product': product}
    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'stock': product.stock,
            'brand': product.brand,
            'is_featured': product.is_featured,
            'user_id': product.user.id if product.user else None,
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)


def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'stock': product.stock,
            'brand': product.brand,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

    
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', datetime.datetime.now().strftime("%d %b %Y, %H:%M"))
            return response
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    form = ProductForm(request.POST or None, instance=product)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('main:show_main')
    context = {"form": form, "product": product}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    if request.method == "POST":
        product.delete()
        return redirect('main:show_main')
    context = {"product": product}
    return render(request, "confirm_delete.html", context)

@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = strip_tags(request.POST.get("name"))  
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description")) 
    category = request.POST.get("category")
    stock = request.POST.get("stock")
    brand = strip_tags(request.POST.get("brand"))  
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'
    user = request.user if request.user.is_authenticated else None

    new_product = Product(
        name=name,
        price=price,
        description=description,
        category=category,
        stock=stock,
        brand=brand,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user,
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
def edit_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    product.name = strip_tags(request.POST.get("name"))
    product.price = request.POST.get("price")
    product.description = strip_tags(request.POST.get("description"))
    product.thumbnail = request.POST.get("thumbnail")
    product.category = request.POST.get("category")
    product.stock = request.POST.get("stock")
    product.brand = strip_tags(request.POST.get("brand"))
    product.is_featured = request.POST.get("is_featured") == "on"
    product.save()
    return HttpResponse(b"UPDATED", status=200)

@csrf_exempt
@require_POST
def delete_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponse(b"DELETED", status=200)

@csrf_exempt
@require_POST
def login_user_ajax(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"message": "Login berhasil!"}, status=200)
    else:
        return JsonResponse({"error": "Username atau password salah."}, status=401)


@csrf_exempt
@require_POST
def register_user_ajax(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    confirm_password = request.POST.get("confirm_password")

    if password != confirm_password:
        return JsonResponse({"error": "Password tidak cocok!"}, status=400)
    if User.objects.filter(username=username).exists():
        return JsonResponse({"error": "Username sudah digunakan!"}, status=400)

    User.objects.create_user(username=username, password=password)
    return JsonResponse({"message": "Registrasi berhasil!"}, status=201)


@csrf_exempt
@require_POST
def logout_user_ajax(request):
    logout(request)
    return JsonResponse({"message": "Logout berhasil!"}, status=200)
