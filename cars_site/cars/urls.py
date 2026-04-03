from django.urls import path
from.import views

urlpatterns = [
    path('', views.home),
    path('cars/', views.cars),
    path('cars/add/', views.add_cars),
    path('cars/search/', views.search_cars),
]