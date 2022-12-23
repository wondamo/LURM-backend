from django.shortcuts import render
from rest_framework import views, viewsets, filters, permissions, generics, status, response
from .serializers import *

# Create your views here.
class LoginView(generics.GenericAPIView):
    '''
    This is the login view for the application for all users
    '''
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class PastQuestionViewset(viewsets.ModelViewSet):
    serializer_class = PastQuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = PastQuestion.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['courseCode']
