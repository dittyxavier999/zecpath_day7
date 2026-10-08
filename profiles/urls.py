from django.urls import path

from .views import (
    CandidateProfileView,
    EmployerProfileView,
    AdminCandidateProfileView,
    AdminEmployerProfileView,
)


urlpatterns = [
    path(
        "candidate/",
        CandidateProfileView.as_view(),
        name="candidate-profile"
    ),
    path(
        "employer/",
        EmployerProfileView.as_view(),
        name="employer-profile"
    ),
    path(
        "admin/candidate/<int:user_id>/",
        AdminCandidateProfileView.as_view(),
        name="admin-candidate-profile"
    ),
    path(
        "admin/employer/<int:user_id>/",
        AdminEmployerProfileView.as_view(),
        name="admin-employer-profile"
    ),
]