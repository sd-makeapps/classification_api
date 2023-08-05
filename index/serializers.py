from rest_framework import serializers

class IndexSerializer(serializers.Serializer):
    input_file = serializers.FileField()