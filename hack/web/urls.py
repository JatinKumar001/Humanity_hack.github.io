from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="web"),
    path("event/", views.event, name="eventpage"),
    path("eventpost/", views.eventpost, name="eventpage"),
    path("sign/", views.sign, name="sign"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
]