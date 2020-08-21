from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "ShopHome"),
    path("dashboard/", views.dashboard, name = "Dashboard"),
    path("addform/", views.addform, name = "AddForm"),
    path("login/", views.login, name = "Login"),
    path("logout/", views.logout, name = "Logout"),
    path("signup/", views.signup, name = "SignUp"),
    path("success/", views.success, name = "Success"),
    path("error/", views.error, name = "Error"),
    path("transaction/", views.transaction, name = "Transaction"),
    path("cart/", views.cart, name = "Cart"),
    path("checkout/", views.checkout, name = "Checkout"),
    path("productview/<int:myid>", views.productview, name = "ProductView"),



]