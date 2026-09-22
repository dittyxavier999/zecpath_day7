from django.contrib import admin
from .models import User, Candidate, Employer, Job, Application


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "username",
        "role",
        "is_active",
        "is_verified",
        "created_at",
    )

    list_filter = (
        "role",
        "is_active",
        "is_verified",
    )

    search_fields = (
        "email",
        "username",
        "phone",
    )


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "skills",
    )

    search_fields = (
        "user__email",
        "user__username",
        "skills",
    )

@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "company_name",
        "company_email",
    )

    search_fields = (
        "user__email",
        "user__username",
        "company_name",
        "company_email",
    )


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "employer",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
    )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "candidate",
        "job",
        "applied_at",
    )