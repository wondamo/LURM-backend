from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

appname='pastquestion'

router = DefaultRouter()

urlpatterns = [
    path('', PastQuestionViewset.as_view({'get':'list'}), name='pastquestion'),
    path('<str:pk>/download/', PastQuestionViewset.as_view({'get':'retrieve'}), name='download'),
    path('upload/', PastQuestionViewset.as_view({'post':'create'}), name='upload'),
]
