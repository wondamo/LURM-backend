from django.shortcuts import render
from rest_framework import views, viewsets, generics
from .serializers import *

# Create your views here.
class PastQuestionViewset(viewsets.ModelViewSet):
    serializer_class = PastQuestionSerializer
    queryset = PastQuestion.objects.all()
