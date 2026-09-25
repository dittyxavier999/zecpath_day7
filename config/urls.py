"""
URL configuration for config project.
"""

from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


def home(request):
    return JsonResponse({
        "message": "Zecpath API is running"
    })


urlpatterns = [
    # Home
    path("", home, name="home"),

    # Django Admin
    path("admin/", admin.site.urls),

    # JWT Login
    path(
        "api/auth/login/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),

    # JWT Refresh
    path(
        "api/auth/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),

    # Users API
    path("api/", include("apps.users.urls")),
]