
from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('signup_user', views.register_user, name="signUp"),
]
