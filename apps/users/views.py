from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import get_user_message


class UserTestView(APIView):
    def get(self, request):
        message = get_user_message()
        return Response({"message": message})