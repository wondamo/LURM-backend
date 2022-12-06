from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

appname='pastquestion'

router = DefaultRouter()

urlpatterns = [
    path('search/', PastQuestionViewset.as_view({'get':'list'}), name='pastquestion'),
    path('download/', PastQuestionViewset.as_view({'get':'retrieve'}), name='download'),
    path('upload/', PastQuestionViewset.as_view({'post':'create'}), name='upload'),
]
