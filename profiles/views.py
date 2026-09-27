from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.permissions import IsCandidate, IsEmployer

from .models import CandidateProfile, EmployerProfile
from .serializers import (
    CandidateProfileSerializer,
    EmployerProfileSerializer,
)


class CandidateProfileView(APIView):
    permission_classes = [IsAuthenticated, IsCandidate]

    def get(self, request):
        profile = CandidateProfile.objects.filter(
            user=request.user,
            is_deleted=False
        ).first()

        if not profile:
            return Response(
                {"detail": "Candidate profile not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CandidateProfileSerializer(profile)

        return Response(serializer.data)

    def post(self, request):
        existing_profile = CandidateProfile.objects.filter(
            user=request.user
        ).first()

        if existing_profile:
            return Response(
                {"detail": "Candidate profile already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CandidateProfileSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save(user=request.user)

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request):
        profile = CandidateProfile.objects.filter(
            user=request.user,
            is_deleted=False
        ).first()

        if not profile:
            return Response(
                {"detail": "Candidate profile not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CandidateProfileSerializer(
            profile,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request):
        profile = CandidateProfile.objects.filter(
            user=request.user,
            is_deleted=False
        ).first()

        if not profile:
            return Response(
                {"detail": "Candidate profile not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        profile.is_deleted = True
        profile.save()

        return Response(
            {"detail": "Candidate profile deleted successfully."},
            status=status.HTTP_200_OK
        )


class EmployerProfileView(APIView):
    permission_classes = [IsAuthenticated, IsEmployer]

    def get(self, request):
        profile = EmployerProfile.objects.filter(
            user=request.user,
            is_deleted=False
        ).first()

        if not profile:
            return Response(
                {"detail": "Employer profile not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = EmployerProfileSerializer(profile)

        return Response(serializer.data)

    def post(self, request):
        existing_profile = EmployerProfile.objects.filter(
            user=request.user
        ).first()

        if existing_profile:
            return Response(
                {"detail": "Employer profile already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = EmployerProfileSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save(user=request.user)

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request):
        profile = EmployerProfile.objects.filter(
            user=request.user,
            is_deleted=False
        ).first()

        if not profile:
            return Response(
                {"detail": "Employer profile not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = EmployerProfileSerializer(
            profile,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request):
        profile = EmployerProfile.objects.filter(
            user=request.user,
            is_deleted=False
        ).first()

        if not profile:
            return Response(
                {"detail": "Employer profile not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        profile.is_deleted = True
        profile.save()

        return Response(
            {"detail": "Employer profile deleted successfully."},
            status=status.HTTP_200_OK
        )