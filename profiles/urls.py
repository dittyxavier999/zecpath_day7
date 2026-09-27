from django.urls import path

from .views import CandidateProfileView, EmployerProfileView


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
]