from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import AddListingForm
from .models import User, Auction_Listings


def index(request):
    return render(request, "auctions/index.html", {
        "list": Auction_Listings.objects.all()
    })
    

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create(request):
    if request.method == "GET":
        form = AddListingForm()
        return render(request, "auctions/create.html", {
            "form": form
        })
    else:
        form = AddListingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            if not post.image:
                post.image="https://freepikpsd.com/wp-content/uploads/2019/10/post-it-png-transparent-1-Transparent-Images.png"
            post.save()
            return HttpResponseRedirect(reverse('index'))
        else: 
            return render(request, "auctions/create.html", {
                "message": "Invalid Post"
            })
    
def info(request, item_id):
    pass
    #remember to add default image if user didn't input