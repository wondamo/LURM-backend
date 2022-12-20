import mimetypes
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import PastQuestion
from django.db import IntegrityError
from drf_base64.fields import Base64FileField


def validate_file(file):
    accepted = ['application/pdf']
    if file.size > 1048576:
            raise serializers.ValidationError("File size must not be larger than 1MB")
    try:
        if file.content_type not in accepted:
            raise serializers.ValidationError(f"{file.content_type} is not a supported format, supported format include: pdf, jpeg, jpg, png")
    except AttributeError:
        file_type = mimetypes.guess_type(file.name)
        if file_type[0] not in accepted:
            raise serializers.ValidationError(f"{file_type[0]} is not a supported format, supported format include: pdf, jpeg, jpg, png")

# Create your serializers here

class PastQuestionSerializer(ModelSerializer):
    questionFile = Base64FileField(required=True, validators=[validate_file])
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

