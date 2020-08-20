from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "ShopHome"),
    path("dashboard/", views.dashboard, name = "Dashboard"),
    path("addform/", views.addform, name = "AddForm"),
    path("login/", views.login, name = "Login"),
    path("signup/", views.signup, name = "SignUp"),
    path("success/", views.success, name = "Success"),
    path("cart/", views.cart, name = "Cart"),
    path("checkout/", views.checkout, name = "Checkout"),
    # path("ch/", views.ch, name = "Ch"),
    path("search", views.search, name = "Search"),
    path("tracker/", views.tracker, name = "TrackingStatus"),
    path("products/", views.productview, name = "ProductView"),



]