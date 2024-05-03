from rest_framework import serializers 
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import refreshtoken


class SingUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','password')

        extra_kwargs = {
            'first_name' : {'required':True, 'allow_blank':False}
            ,'last_name' : {'required':True, 'allow_blank':False}
            ,'email' : {'required':True, 'allow_blank':False}
            ,'password' : {'required':True, 'allow_blank':False , 'max_length':8}
        }







class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        ref = refreshtoken.objects.create(
            refresh = token,
            user= user
        )

        return token