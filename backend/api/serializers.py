from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note
from .models import Graph

# ORM Object Relational Mapping
# Maps python objects to corresponding code
# Serializers use apis to utilize jsons (requesting and responses)
# Converts python object to json data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only":True}}

class GraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Graph
        fields= [
            "id",
            "number",
            "author",
            "created_at"
        ]
        extra_kwargs = {"author": {"read_only":True}}

        