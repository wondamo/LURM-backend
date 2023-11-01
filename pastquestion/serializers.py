import mimetypes
from rest_framework import serializers, exceptions
from rest_framework.serializers import ModelSerializer
from .models import *
from django.db import IntegrityError
from drf_base64.fields import Base64FileField
from django.contrib.auth import authenticate


def validate_file(file):
    accepted = ['application/pdf']
    if file.size > 1048576:
            raise serializers.ValidationError("File size must not be larger than 1MB")
    try:
        if file.content_type not in accepted:
            raise serializers.ValidationError(f"{file.content_type} is not supported, only pdf is supported.")
    except AttributeError:
        file_type = mimetypes.guess_type(file.name)
        if file_type[0] not in accepted:
            raise serializers.ValidationError(f"{file_type[0]} is not supported, only pdf is supported.")

# Create your serializers here
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=68, write_only=True)
    tokens = serializers.SerializerMethodField()

    def validate(self, data):
        username, password = data['username'], data['password']
        user = User.objects.get(username=username)
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed("Invalid credentials try again")
        return data

    def get_tokens(self, obj):
        user = User.objects.get(username=obj['username'])
        return user.tokens()


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
            raise serializers.ValidationError("You can't upload the same past questions more than once")
        return pq

