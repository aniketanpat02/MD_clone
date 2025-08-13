from rest_framework import serializers
from firstapp.models import Center

class CenterSerializer(serializers.Serializer):
    code = serializers.IntegerField()
    short_name = serializers.CharField()
    name = serializers.CharField()
    phone = serializers.IntegerField()
    village = serializers.CharField()

    class Meta:
        model= Center
        fields = "__all__"