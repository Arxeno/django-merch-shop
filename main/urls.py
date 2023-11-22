from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_landing, name='display_landing'),
    path('uploads/<str:filename>', views.send_image),
    path('create/item', views.create_item, name='create_item'),
    path('item/xml', views.show_xml),
    path('item/xml/<str:id>', views.show_xml_by_id),
    path('item/json', views.show_json, name='get_items_json'),
    path('item/json/<str:id>', views.show_json_by_id),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('edit/item', views.edit_item, name='edit_item'),
    path('category/<str:category_id>',
         views.get_category_id, name='get_category_id'),
    path('category', views.get_category, name="get_category"),
    path('create-ajax', views.create_item_ajax, name='create_item_ajax'),
    path('create-flutter/', views.create_product_flutter,
         name='create_product_flutter')
]
