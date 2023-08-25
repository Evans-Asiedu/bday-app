from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    
    path("doctors", views.doctors, name="doctors"),
    path("exercises", views.exercises, name="exercises"),
    path("dieting", views.dieting, name="dieting"),
  
    path("doctors/<int:doctor_id>", views.bookappointment, name="bookappointment"),
    path("appointment", views.appointments, name="appointment"),
    path("appointment/<int:appointment_id>", views.appointment, name="appointment"),

    path("create_post", views.create_post, name="create_post"),
    path("like/<int:post_id>", views.like_post, name="like"),
    path("favouritepost", views.favourite_post, name="favouritepost"),
]