from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('signin/', views.get_username, name='get_username'),
  path('chat/<str:name>/', views.chat_page, name='chat_page'),
]