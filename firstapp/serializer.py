from rest_framework import serializers
from firstapp.models import Center ,Customer, Collection

class CenterSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    code = serializers.IntegerField()
    short_name = serializers.CharField()
    name = serializers.CharField()
    phone = serializers.IntegerField()
    village = serializers.CharField()
    status = serializers.IntegerField()

    class Meta:
        model= Center
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = "__all__"


class CollectionSerializer(serializers.ModelSerializer):
    center = CenterSerializer(read_only=True)
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Collection
        fields ="__all__"

"""


"""
