from django.urls import path
from .views import *

urlpatterns = [
    path("", index_page, name="index"),
    path("login/", login_page, name="login"),
    path("signup/", signup_page, name="signup"),
    path("home/", home_page, name="home"),
    path("logout/", logout_page, name="logout"),
    path("update/<int:id>", update_page, name="update"),
    path("delete/<int:id>", delete_page, name = "delete"),
    path("add-student/", add_student, name="add-student"),
]
