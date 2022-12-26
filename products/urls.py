# Django
from django.urls import path

# Aps
from .views import ViewProdutsView, RegisterProductFormView, ProductosDeleteView, UpdateProductFormView

urlpatterns = [
    path('', ViewProdutsView.as_view()),
    path('register', RegisterProductFormView.as_view()),
    path('<pk>/delete/', ProductosDeleteView.as_view()),
    path('<pk>/update/', UpdateProductFormView.as_view()),
]
