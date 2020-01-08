from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "ShopHome"),
    path("about/", views.about, name = "AboutUs"),
    path("contact/", views.contact, name = "ContactUs"),
    path("search/", views.search, name = "Search"),
    path("products/<int:myid>", views.productView, name = "ProductView"),
    path("veg/", views.veg, name = "Veg"),
    path("nonveg/", views.nonveg, name = "Non-veg"),
]
