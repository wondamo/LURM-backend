from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

appname='pastquestion'

router = DefaultRouter()

pastquestion = SearchPastQuestion.as_view({
    'post':'create',
    'get':'retrieve',
    'get':'list',
})

urlpatterns = [
    path('', pastquestion, name='pastquestion')
]
