from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "ShopHome"),
    path("contact/", views.contact, name = "ContactUs"),
    path("login/", views.login, name = "Login"),
    path("signup/", views.signup, name = "SignUp"),
    path("checkout/", views.checkout, name = "Checkout"),
    path("search", views.search, name = "Search"),
    path("tracker/", views.tracker, name = "TrackingStatus"),
    path("products/", views.productview, name = "ProductView"),



]