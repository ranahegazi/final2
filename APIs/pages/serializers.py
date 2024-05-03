from rest_framework import serializers
from .models import comments,suggestions


class commentSerializer(serializers.ModelSerializer):

    class Meta:
        model = comments
        fields = "__all__"



class suggestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = suggestions
        fields = "__all__"