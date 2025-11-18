from django.urls import path
from main.views import show_main, add_product, show_description, show_xml, show_json, show_xml_by_id, show_json_by_id, proxy_image
from main.views import register, login_user, logout_user, edit_product, delete_product, add_product_ajax, edit_product_ajax, login_ajax, register_ajax, delete_product_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('add_product/', add_product, name='add_product'),
    path('add_product_ajax/', add_product_ajax, name='add_product_ajax'),
    path('product/<str:id>/', show_description, name='show_description'),
    path('register/', register, name='register'),
    path('register_ajax/', register_ajax, name='register_ajax'),
    path('login/', login_user, name='login'),
    path('login_ajax/', login_ajax, name='login_ajax'),
    path('logout/', logout_user, name='logout'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/edit_ajax', edit_product_ajax, name='edit_product_ajax'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path('product/<uuid:id>/delete_ajax', delete_product_ajax, name='delete_product_ajax'),
    path('proxy-image/', proxy_image, name='proxy_image'),
]