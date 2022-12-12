from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import PastQuestion
from django.db import IntegrityError
from drf_base64.fields import Base64ImageField

# Create your serializers here

class PastQuestionSerializer(ModelSerializer):
    questionFile = Base64ImageField(required=True)
    class Meta:
        model=PastQuestion
        fields = ['courseCode', 'semester', 'level', 'session', 'questionFile']

    def create(self, validated_data):
        try:
            pq = self.Meta.model.objects.create(**validated_data)
            pq.save()
        except IntegrityError:
            raise serializers.ValidationError("You can upload the same past questions more than once")
        return pq