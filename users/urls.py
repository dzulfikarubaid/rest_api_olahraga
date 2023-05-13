from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('add/', views.Add, name='add'),
    path('list/',views.List, name='list'),
    path('update/<int:id>/',views.Update, name='update'),
    path('delete/<int:id>/',views.Delete, name='delete'),
]