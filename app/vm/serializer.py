from rest_framework import serializers
from .models import VM


class VMSerializer(serializers.ModelSerializer):
    names = serializers.CharField(source='name')

    class Meta:
        model = VM
        fields = ("id", "names")
