from django.conf import settings
from django.shortcuts import render, redirect
from django.http import FileResponse, Http404, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, HttpResponseServerError, JsonResponse
from .models import Category, Item
from .forms import ItemForm
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse

# Create your views here.


@login_required(login_url='/login')
def display_landing(request):
    try:
        items = Item.objects.all()
    except:
        return HttpResponseServerError()

    try:
        context = {
            'items': items,
            'last_login': request.COOKIES['last_login'],
            'name': request.user.username
        }
    except:
        return redirect('main:login')

    return render(request, 'index.html', context)


def send_image(request, filename):
    try:
        file = open(f'{settings.MEDIA_ROOT}/uploads/{filename}', 'rb')
        response = FileResponse(file)

        ext = filename.split('.')[-1]
        if (ext == 'png'):
            response['Content-Type'] = 'image/png'
        elif (ext in ['jpg', 'jpeg']):
            response['Content-Type'] = 'image/jpeg'
        elif (ext == 'webp'):
            response['Content-Type'] = 'image/webp'

        return response
    except:
        return JsonResponse({"message": "Not found."}, status=404)


@login_required(login_url='/login')
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        user = request.user
        name = form.cleaned_data['name']
        amount = form.cleaned_data['amount']
        description = form.cleaned_data['description']
        price = form.cleaned_data['price']
        category = form.cleaned_data['category']
        image = request.FILES['image']
        new_item = Item(user=user, name=name, amount=amount, description=description,
                        price=price, category=category, image=image)
        new_item.save()
        # form.save()
        return render(request, 'success.html')

    context = {'form': form}
    return render(request, 'create_item.html', context)


def show_xml(request):
    items = Item.objects.all()
    return HttpResponse(serializers.serialize('xml', items), content_type='application/xml')


def show_xml_by_id(request, id):
    item = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('xml', item), content_type='application/xml')


def show_json(request):
    items = Item.objects.all()
    return HttpResponse(serializers.serialize('json', items), content_type='application/json')


def show_json_by_id(request, id):
    item = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', item), content_type='application/json')


def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sukses membuat akun!')
            return redirect('main:login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('main:display_landing'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(
                request, 'Maaf, entry username atau password salah. Silahkan coba lagi.')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


def edit_item(request):
    if request.method == 'POST':
        request = request.POST.get('action').split('$')
        action = request[0]
        item_id = request[1]

        try:
            item = Item.objects.get(pk=item_id)
        except:
            return Http404('MODEL NOT FOUND')

        if action == 'add':
            item.amount += 1
            item.save()
            return redirect('main:display_landing')
        elif action == 'substract':
            if (item.amount > 0):
                item.amount -= 1
            item.save()
            return redirect('main:display_landing')
        else:
            return HttpResponseBadRequest('BAD REQUEST')
    elif request.method == 'DELETE':
        item_id = request.GET.get('id')

        try:
            item = Item.objects.get(pk=item_id)
        except:
            return Http404('MODEL NOT FOUND')

        item.delete()
        return redirect('main:display_landing')


def get_category_id(request, category_id):
    category = Category.objects.get(pk=category_id)

    return JsonResponse({'categoryName': category.name}, status=200)


def get_category(request):
    items = Category.objects.all()
    return HttpResponse(serializers.serialize('json', items), content_type='application/json')


@login_required(login_url='/login')
def create_item_ajax(request):
    if request.method == 'POST':
        print(request.POST['category'])
        user = request.user
        name = request.POST['name']
        amount = request.POST['amount']
        description = request.POST['description']
        price = request.POST['price']
        category_id = request.POST['category']
        image = request.FILES['image']

        category = Category.objects.get(pk=category_id)

        new_item = Item(user=user, name=name, amount=amount, description=description,
                        price=price, category=category, image=image)
        new_item.save()
        return JsonResponse({'message': 'Success!'}, status=200)
