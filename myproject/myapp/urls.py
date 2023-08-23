from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:name>/<int:id>', views.item, name='item'),
    path('new_index', views.new_index, name='new_index'),
    path('some_data', views.some_data, name='some_data'),
    path('some_data/<int:start>/<int:end>', views.random_data, name='random_data'),
    path('new_instance/<str:name>/<str:description>/<int:price>', views.new_instance, name='new_instance'),
    path('update_instance/<int:id>/<str:name>/<str:description>/<int:price>', views.update_instance, name='update_instance'),
    path('delete_instance/<int:id>/', views.delete_instance, name='delete_instance'),
]