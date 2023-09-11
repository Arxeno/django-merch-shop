from django.shortcuts import render
from django.http import FileResponse, Http404
from .models import Item

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
