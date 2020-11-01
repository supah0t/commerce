from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("<int:item_id>", views.info, name="info"),
    path("<int:item_id>/closed", views.close, name="close"),
    path("<int:item_id>/add", views.add, name="add"),
    path("watchlist", views.watchlist, name="watchlist")
]
