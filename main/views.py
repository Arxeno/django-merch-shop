from django.shortcuts import render, redirect
from django.http import FileResponse, Http404, HttpResponse
from .models import Item
from .forms import ItemForm
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.


def display_landing(request):
    try:
        items = Item.objects.all()
    except:
        return Http404()

    context = {
        'items': items
    }
    return render(request, 'index.html', context)


def send_image(request, category, filename):
    try:
        file = open(f'uploads/{category}/{filename}', 'rb')
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
        return Http404()


def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        print(form)
        print(type(form))
        name = form.cleaned_data['name']
        amount = form.cleaned_data['amount']
        description = form.cleaned_data['description']
        price = form.cleaned_data['price']
        category = form.cleaned_data['category']
        image = request.FILES['image']
        new_item = Item(name=name, amount=amount, description=description,
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
            return redirect('main:display_landing')
        else:
            messages.info(
                request, 'Maaf, entry username atau password salah. Silahkan coba lagi.')
    context = {}
    return render(request, 'login.html', context)
