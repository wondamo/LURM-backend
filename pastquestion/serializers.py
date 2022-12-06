from rest_framework.serializers import ModelSerializer
from .models import PastQuestion

# Create your serializers here

class PastQuestionSerializer(ModelSerializer):
    class Meta:
        model=PastQuestion
        fields = ['courseCode', 'semester', 'level', 'session', 'questionFile']
        extra_kwargs = {'questionFile':{'required':True}}