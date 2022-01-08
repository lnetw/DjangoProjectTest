from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r'^$', views.home_page, name='home_page'),
    path('data/<int:pk>/', views.data_details, name='data_details'),
    path('data/new/', views.new_record, name='new_record'),
    path('data/<int:pk>/edit/', views.record_edit, name='record_edit'),
]
