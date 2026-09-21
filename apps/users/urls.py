from django.urls import path

from .views import UserTestView


urlpatterns = [
    path("test/", UserTestView.as_view(), name="user-test"),
]