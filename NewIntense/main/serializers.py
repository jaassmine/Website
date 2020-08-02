from rest_framework import serializers

from account.serializers import UserSerializer
from .models import *


class JobSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Job
        fields = "__all__"


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = "__all__"