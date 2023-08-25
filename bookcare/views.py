from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.core.paginator import Paginator
from tempus_dominus.widgets import DateTimePicker
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json
from django.contrib.auth.decorators import login_required

from .models import CustomUser
from datetime import datetime
from django.utils import timezone

from .models import CustomUser, Post, Appointment, Like



# paginate pages 
def paginate_page(request, pages):
    paginator = Paginator(pages, 10)
    page_number = request.GET.get('page')
    page_paginated = paginator.get_page(page_number)
    return page_paginated


# Create your views here.
def index(request):
    all_posts = Post.objects.all().order_by("-publication_date") if request.user is not None else []

    user_liked_posts_obj = Like.objects.filter(user=request.user) if request.user.id is not None else []
    user_liked_posts = [post_obj.post for post_obj in user_liked_posts_obj]

    # paginate function called
    posts_paginated = paginate_page(request, all_posts)

    return render(request, "bookcare/index.html", {
        "all_posts": posts_paginated,
        "user_liked_posts": user_liked_posts,
         "title": "All Post"
    })
    

def login_view(request):
    if request.method == "POST":

        #Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        #check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "bookcare/login.html",{
                "message": "Invalid username and/or password"
            })
    else:
        return render(request, "bookcare/login.html")
        

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]
        is_doctor = eval(request.POST.get("is_doctor"))
        about = request.POST.get("about")

        #ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "bookcare/register.html")
    
        # Attempt to create new user
        try:
            user = CustomUser.objects.create_user(
                first_name = firstname,
                last_name = lastname,
                username = username,
                email = email,
                password = password,
                is_doctor = is_doctor,
                about = about
            )
            user.save()

        except IntegrityError:
            return render(request, "bookcare/register.html")
        
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "bookcare/register.html")
    


def doctors(request):
    all_doctors = CustomUser.objects.filter(is_doctor=True).reverse()

    # paginate function called
    doctors_paginated = paginate_page(request, all_doctors)

    return render(request, "bookcare/doctors.html", {
        "all_doctors": doctors_paginated,
    })


def exercises(request):
    all_exercises = Post.objects.filter(category="Exercise").order_by('-publication_date')

    user_liked_posts_obj = Like.objects.filter(user=request.user) if request.user.id is not None else []
    user_liked_posts = [post_obj.post for post_obj in user_liked_posts_obj]

    exercises_paginated = paginate_page(request, all_exercises)

    return render(request, "bookcare/index.html", {
        "all_posts": exercises_paginated,
        "user_liked_posts": user_liked_posts,
         "title": "Exercises"
    })


def dieting(request):
    all_dieting = Post.objects.filter(category="Dieting").order_by('-publication_date')

    user_liked_posts_obj = Like.objects.filter(user=request.user) if request.user.id is not None else []
    user_liked_posts = [post_obj.post for post_obj in user_liked_posts_obj]

    dieting_paginated = paginate_page(request, all_dieting)

    return render(request, "bookcare/index.html", {
        "all_posts": dieting_paginated,
        "user_liked_posts": user_liked_posts,
        "title": "Dieting"
    })


@login_required
def bookappointment(request, doctor_id):
    doctor = CustomUser.objects.get(id=doctor_id)
  
    if request.method == "POST":
        form = BookAppointmentForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data["category"]
            datetime = form.cleaned_data["datetime"]

            appointment = Appointment(
                client = request.user,
                doctor = doctor,
                category = category,
                appointment_date = datetime,
            )
            appointment.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "bookcare/appointmentform.html", {
                "form": form,
                "doctor": doctor,
            })
    else:
        return render(request, "bookcare/appointmentform.html", {
            "form": BookAppointmentForm(),
            "doctor": doctor
            })



def appointments(request):
    user_appointments = Appointment.objects.filter(Q(doctor=request.user) | Q(client=request.user)).order_by('-appointment_date')

    user_appointments_paginated = paginate_page(request, user_appointments)

    return render(request, "bookcare/appointments.html", {
        "all_appointments": user_appointments_paginated,
    })


def appointment(request, appointment_id):
    if request.method == "POST":
        if request.POST.get("delete") == "Delete":
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.delete()
        return HttpResponseRedirect(reverse(appointments))


@login_required
def create_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            # get data from form
            title = form.cleaned_data["title"]
            image = form.cleaned_data["image"]
            content = form.cleaned_data["content"]
            category = form.cleaned_data["category"]

            #create a post
            post = Post(
                user = request.user,
                title = title,
                image = image,
                content = content,
                category = category,
                publication_date = timezone.now(),
            )
            post.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "bookcare/create_post.html",{
                "form": form
            })
    return render(request, "bookcare/create_post.html", {
        "form": CreatePostForm()
    })


def favourite_post(request):
    user_liked_posts_obj = Like.objects.filter(user=request.user).reverse() if request.user.id is not None else []
    user_liked_posts = [post_obj.post for post_obj in user_liked_posts_obj]

    posts_paginated = paginate_page(request, user_liked_posts)

    return render(request, "bookcare/index.html", {
        "all_posts": posts_paginated,
        "user_liked_posts": posts_paginated,
        "title": "Favourite Posts"
    })


@csrf_exempt
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == "PUT":
        data = json.loads(request.body)
        if data.get("like"):
            Like.objects.create(user=request.user, post=post)
        else:
            Like.objects.filter(user=request.user, post=post).delete()

    return HttpResponseRedirect(reverse("index"))



# Forms
class BookAppointmentForm(forms.Form):
    category = forms.ChoiceField(
        label="Which procedure do you want to make an appointment for?",
        choices=Appointment.CATEGORY,
        required=True,
        widget=forms.Select(
            attrs={
                "class": "form-control mb-2"
            }
        )
    )

    datetime = forms.DateTimeField(
        label="Preferred Appointment Date",
        widget=DateTimePicker(
            options={
                'usecurrent': True,
                'collapse': False,
                'format': 'YYYY-MM-DD HH:mm',
                'minDate': datetime.now().strftime("%Y-%m-%d"),
                'maxDate': '2025-12-31',
            },
            attrs={
                'class': 'form-control mt-0',
                'icon_toggle': True,
                'append': 'fas fa-calendar-alt fa-lg',
            }
        )
    )
     
    

class CreatePostForm(forms.ModelForm):
    title = forms.CharField(
        label="Title",
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                "aria-label": "title",
                "class": "form-control mb-2"
            }
        )
    )

    image = forms.URLField(
    label="Image URL",
    required=True,
    widget=forms.URLInput(
        attrs={
            "class": "form-control mb-2"
            }
        )
    )

    content = forms.CharField(
        label="Description",
        widget=forms.Textarea(
            attrs={
                "placeholder": "write about the post",
                "aria-label": "content",
                "class": "form-control mb-2",
                "rows": "4"
            }
        )
    )

    category = forms.ChoiceField(
        label="Categories",
        choices=Post.CATEGORY,
        required=True,
        widget=forms.Select(
            attrs={
                "class": "form-control mb-2"
            }
        )
    )

    class Meta:
        model = Post
        fields = ["title", "image", "content", "category"]
