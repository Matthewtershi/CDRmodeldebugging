from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserSerializer, NoteSerializer, GraphSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note, Graph
import matplotlib.pyplot as plt
import io 
import base64

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # you cant call this route unless you pass a valid (authenticated) JWT token
    # first 2 lines use the serializers.py file to compare Note to specified format for auth

    def get_queryset(self):
        user = self.request.user # gives us user bc we are authenticated
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class GraphListCreate(generics.ListCreateAPIView):
    serializer_class = GraphSerializer
    permission_classes = [IsAuthenticated] 
    
    def get_queryset(self):
        user = self.request.user 
        return Graph.objects.filter(author=user)
    
    def perform_create(self, serializer):
        print("Serializer data:", serializer.initial_data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

    def post(self, request):
        print("Request data:", request.data)
        serializer = GraphSerializer(data=request.data)
        if serializer.is_valid():
            number = serializer.validated_data["number"]
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=400)
        
        x = range(10)
        y = [number * i for i in x]
        plt.figure(figsize=(5, 4))
        plt.plot(x, y, marker="o")
        plt.title(f"Graph for number {number}")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        
        # Convert the graph to a base64 string
        buffer = io.BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.read()).decode("utf-8")
        buffer.close()
        plt.close()

        return Response({"graph": image_base64})

class NoteDelete(generics.DestroyAPIView):
    # queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

