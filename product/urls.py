from django.urls import path
from product import views

urlpatterns = [
    path("action/", views.ProductManagement.as_view()),
    ]