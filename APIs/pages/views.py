from django.shortcuts import render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import comments,suggestions
from .serializers import commentSerializer,suggestionSerializer




# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment(request):
    data = request.data
    serializer = commentSerializer(data = data)
    if serializer.is_valid():
       comment = comments.objects.create(**data,user=request.user)
       res = commentSerializer(comment,many=False)
       return Response({"comment":res.data})
    
    else:
        return Response(serializer.errors)
    





@api_view(['POST'])
@permission_classes([IsAuthenticated])
def suggestion(request):
    data = request.data
    serializer = suggestionSerializer(data = data)
    if serializer.is_valid():
       suggestion = suggestions.objects.create(**data,user=request.user)
       res = suggestionSerializer(suggestion,many=False)
       return Response({"product":res.data})
    
    else:
        return Response(serializer.errors)