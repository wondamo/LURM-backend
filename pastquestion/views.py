from django.shortcuts import render
from rest_framework import views, viewsets, generics
from .serializers import PastQuestionSerializer

# Create your views here.
class SearchPastQuestion(viewsets.ModelViewSet):
    serializer_class = PastQuestionSerializer
