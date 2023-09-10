from django.shortcuts import render

# Create your views here.


def display_landing(request):
    return render(request, 'index.html')
