from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "ShopHome"),
    path("admin/", views.admin, name = "AdminPage"),
    path("addform/", views.addform, name = "AddForm"),
    path("login/", views.login, name = "Login"),
    path("signup/", views.signup, name = "SignUp"),
    path("success/", views.success, name = "success"),
    path("checkout/", views.checkout, name = "Checkout"),
    path("search", views.search, name = "Search"),
    path("tracker/", views.tracker, name = "TrackingStatus"),
    path("products/", views.productview, name = "ProductView"),



]