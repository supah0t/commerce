from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import AddListingForm, Comment_Form, Bid_Form
from .models import User, Auction_Listings, Comment


def index(request):
    return render(request, "auctions/index.html", {
        "list": Auction_Listings.objects.all().order_by('-id')
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
                post.image="https://semantic-ui.com/images/wireframe/image.png"
            post.save()
            return HttpResponseRedirect(reverse('index'))
        else: 
            return render(request, "auctions/create.html", {
                "message": "Invalid Post"
            })
    
def info(request, item_id):
    if request.method == "GET":
        form = Comment_Form()
        bid_form = Bid_Form()
        item = Auction_Listings.objects.get(pk=item_id)
        user = request.user
        loged = False
        isOwner = False
        winner = False
        watching = False
        comments = Comment.objects.filter(item=item)
        if request.user.is_authenticated:
            loged = True
            if (item in user.watchlist.all()):
                watching = True
            if user == item.user:
                isOwner = True
        if item.winner == user:
            winner = True
        return render(request, "auctions/info.html", {
            'item': item,
            'user': user,
            'loged': loged,
            'isOwner': isOwner,
            'isWinner': winner,
            'form': form,
            'comments': comments,
            'watching': watching,
            'bid_form': bid_form
        })
    else:
        form = Comment_Form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            item = Auction_Listings.objects.get(pk=item_id)
            post.item = item
            post.poster = request.user
            post.save()
            return HttpResponseRedirect(reverse('info', kwargs={'item_id': item_id}))

def close(request, item_id):
    item = Auction_Listings.objects.get(pk=item_id)
    item.closed = True
    item.save()
    return HttpResponseRedirect(reverse('info', kwargs={'item_id': item_id}))


def add(request, item_id):
    item = Auction_Listings.objects.get(pk=item_id)
    user = request.user
    user.watchlist.add(item)
    return HttpResponseRedirect(reverse('info', kwargs={'item_id': item_id}))
    
def remove(request, item_id):
    item = Auction_Listings.objects.get(pk=item_id)
    user = request.user
    user.watchlist.remove(item)
    return HttpResponseRedirect(reverse('watchlist'))

def watchlist(request):
    person = request.user
    watchlist = person.watchlist.all()
    return render(request, 'auctions/watchlist.html', {
        'watchlist': watchlist
    })
    
def bid(request, item_id):
    if request.method=="POST":
        form = Bid_Form(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            item = Auction_Listings.objects.get(pk=item_id)
            if bid.starting_bid < item.starting_bid:
                return HttpResponseRedirect(reverse('info', kwargs={'item_id': item_id}))
            else:
                item.starting_bid = bid.starting_bid
                item.winner = request.user
                item.save()
                return HttpResponseRedirect(reverse('info', kwargs={'item_id': item_id}))

def category(request, category):
    items = Auction_Listings.objects.filter(category=category)
    return render(request, 'auctions/category.html', {
        'list': items,
        'category': category
    })