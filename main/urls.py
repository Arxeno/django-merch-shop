from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_landing),
    path('uploads/<str:category>/<str:filename>', views.send_image),
    path('create/item', views.create_item, name='create_item'),
    path('item/xml', views.show_xml),
    path('item/xml/<str:id>', views.show_xml_by_id),
    path('item/json', views.show_json),
    path('item/json/<str:id>', views.show_json_by_id),
    path('register/', views.register, name='register')
]
