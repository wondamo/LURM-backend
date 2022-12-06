from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import PastQuestion
from django.db import IntegrityError

# Create your serializers here

class PastQuestionSerializer(ModelSerializer):
    class Meta:
        model=PastQuestion
        fields = ['courseCode', 'semester', 'level', 'session', 'questionFile']
        extra_kwargs = {'questionFile':{'required':True}}

    def create(self, validated_data):
        try:
            pq = self.Meta.model.objects.create(**validated_data)
            pq.save()
        except IntegrityError:
            raise serializers.ValidationError("You can upload the same past questions more than once")
        return pq