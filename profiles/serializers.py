from rest_framework import serializers

from .models import CandidateProfile, EmployerProfile


class CandidateProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CandidateProfile
        fields = [
            "id",
            "user",
            "skills",
            "education",
            "experience",
            "expected_salary",
            "is_deleted",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "is_deleted",
            "created_at",
            "updated_at",
        ]


class EmployerProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployerProfile
        fields = [
            "id",
            "user",
            "company_name",
            "domain",
            "company_size",
            "is_verified",
            "is_deleted",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "is_verified",
            "is_deleted",
            "created_at",
            "updated_at",
        ]