from django.contrib import admin
from django.urls import path,include
from .views import home,log_list,update_log,delete_log,create_log,log_detail

urlpatterns = [
    path('', home, name='home'),
    path('list/', log_list, name='log_list'),
    path('list/<int:pk>/', log_detail, name='log_detail'),
    path('add/', create_log, name='create_log'),
    path('list/<int:pk>/update/', update_log, name='update_log'),
    path('list/<int:pk>/delete/', delete_log, name='delete_log'),
]