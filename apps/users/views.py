from django.shortcuts import render

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken

from .permissions import IsAdmin, IsEmployer, IsCandidate
from .serializers import RegisterSerializer
from .services import get_user_message


class UserTestView(APIView):
    """
    Basic test endpoint.
    """

    def get(self, request):
        message = get_user_message()

        return Response({
            "message": message
        })


class ProfileView(APIView):
    """
    JWT-protected endpoint.

    Only authenticated users can access this API.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": "You are authenticated!",
            "username": request.user.username,
            "email": request.user.email,
            "role": request.user.role,
        })


class RegisterView(APIView):
    """
    API endpoint for registering a new user.
    """

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            return Response(
                {
                    "message": "User registered successfully.",
                    "username": user.username,
                    "email": user.email,
                    "role": user.role,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class AdminTestView(APIView):
    """
    Test endpoint accessible only by administrators.
    """

    permission_classes = [IsAdmin]

    def get(self, request):
        return Response({
            "message": "Admin access granted.",
            "role": request.user.role
        })


class EmployerTestView(APIView):
    """
    Test endpoint accessible only by employers.
    """

    permission_classes = [IsEmployer]

    def get(self, request):
        return Response({
            "message": "Employer access granted.",
            "role": request.user.role
        })


class CandidateTestView(APIView):
    """
    Test endpoint accessible only by candidates.
    """

    permission_classes = [IsCandidate]

    def get(self, request):
        return Response({
            "message": "Candidate access granted.",
            "role": request.user.role
        })


class JobCreateView(APIView):
    """
    Endpoint for creating a job.

    Only employers can create jobs.
    """

    permission_classes = [IsEmployer]

    def post(self, request):
        return Response({
            "message": "Employer can create a job.",
            "user": request.user.username,
            "role": request.user.role,
        })


class LogoutView(APIView):
    """
    API endpoint for logging out a user.

    The refresh token is blacklisted so it
    cannot be used to obtain another access token.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response(
                {
                    "error": "Refresh token is required."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {
                    "message": "Logout successful."
                },
                status=status.HTTP_200_OK,
            )

        except Exception:
            return Response(
                {
                    "error": "Invalid or expired refresh token."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )