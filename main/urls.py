from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_landing),
    path('uploads/<str:category>/<str:filename>', views.send_image)
]
