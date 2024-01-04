from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createauction", views.createAuction, name="createauction"),
    path("searchByCategory", views.searchByCategory, name="searchByCategory"),
    path("auction/<int:id>", views.auction, name="auction"),
    path("removeFromWatchlist/<int:id>", views.removeFromWatchlist, name="removeFromWatchlist"),
    path("addFromWatchlist/<int:id>", views.addFromWatchlist, name="addFromWatchlist"),
    path("showWatchlist", views.showWatchList, name="showWatchlist"),
    path("sendComment/<int:id>", views.sendComment, name="sendComment"),
    path("sendBid/<int:id>", views.sendBid, name="sendBid"),
    path("endAuction/<int:id>", views.endAuction, name="endAuction")
]
