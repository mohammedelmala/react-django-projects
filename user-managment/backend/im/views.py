from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.decorators import action
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer


# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=["POST"])
    def register(self, request):
        data = request.data
        try:
            username = data["username"]
            password = make_password(data["password"])
            first_name = data["first_name"]
            last_name = data["last_name"]
            email = data["email"]
            is_active = True
            is_staff = True
            user = User.objects.create(username=username,
                                       password=password,
                                       email=email,
                                       first_name=first_name,
                                       last_name=last_name,
                                       is_active=is_active,
                                       is_staff=is_staff)
            serializer = UserSerializer(user, many=False)
            response = {"message": "Register completed successfully.","data":serializer.data}
            response_status = status.HTTP_200_OK
        except Exception as e:
            response = {"message":str(e), "error": True}
            response_status = status.HTTP_400_BAD_REQUEST

        return Response(response, status=response_status)

