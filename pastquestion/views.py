from django.shortcuts import render
from rest_framework import views, viewsets, generics
from .serializers import PastQuestionSerializer

# Create your views here.
class PastQuestion(viewsets.ModelViewSet):
    serializer_class = PastQuestionSerializer
