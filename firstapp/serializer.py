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

    class Meta:
        model = Collection
        fields ="__all__"

"""

from rest_framework import serializers

class CollectionSerializer(serializers.Serializer):
    date = serializers.DateField()
    type = serializers.CharField()
    shift = serializers.CharField()
    quantity = serializers.DecimalField(max_digits=3, decimal_places=2)
    snf = serializers.DecimalField(max_digits=4, decimal_places=2)
    fat = serializers.DecimalField(max_digits=4, decimal_places=2)
    rate = serializers.DecimalField(max_digits=4, decimal_places=2)

    def to_representation(self, instance):
        return {
            "date": instance.date,
            "type": instance.type,
            "shift": instance.shift,
            "quantity": instance.quantity,
            "snf": instance.snf,
            "fat": instance.fat,
            "rate": instance.rate,
        }
"""
