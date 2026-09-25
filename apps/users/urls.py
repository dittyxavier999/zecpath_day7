from django.urls import path

from .views import (
    LogoutView,
    ProfileView,
    RegisterView,
    UserTestView,
    AdminTestView,
    EmployerTestView,
    CandidateTestView,
)

urlpatterns = [
    path("test/", UserTestView.as_view(), name="user-test"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("auth/register/", RegisterView.as_view(),name="register"),
    path("auth/logout/",LogoutView.as_view(),name="logout"),

    path("test/admin/", AdminTestView.as_view()),
    path("test/employer/", EmployerTestView.as_view()),
    path("test/candidate/", CandidateTestView.as_view())
]