from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .serializers import SingUpSerializer , MyTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
@api_view(['POST'])
def register(request):
    data = request.data
    user = SingUpSerializer(data=data)

    if user.is_valid():
        if not User.objects.filter(email=data['email']).exists():
            user =User.objects.create(
                first_name = data['first_name'],
                last_name = data['last_name'],
                email = data['email'],
                username = data['email'],
                password = make_password(data['password']),
            )
            return Response(
                {'details':'your account is registered'},
                
            )
        else:
             return Response(
                {'details':'your account is already exist'},
                
            )
    else:
        return Response(user.errors)
    




class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer