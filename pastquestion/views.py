from django.shortcuts import render
from rest_framework import views, viewsets, filters, permissions
from .serializers import *

# Create your views here.
class PastQuestionViewset(viewsets.ModelViewSet):
    serializer_class = PastQuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = PastQuestion.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['courseCode']
