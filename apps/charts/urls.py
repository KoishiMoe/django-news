from django.urls import path

from . import views

urlpatterns = [
    path("stock_complex/", views.stock_complex, name="stock_complex"),
    path("stock_simple/", views.stock_simple, name="stock_simple"),
]
