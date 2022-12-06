from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

appname='pastquestion'

router = DefaultRouter()

urlpatterns = [
    path('search/', PastQuestion.as_view({'get':'list'}), name='pastquestion'),
    path('download/', PastQuestion.as_view({'get':'retrieve'}), name='download'),
    path('upload/', PastQuestion.as_view({'post':'create'}), name='upload'),
]
