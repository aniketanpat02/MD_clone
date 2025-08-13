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


class CustomerSerializer(serializers.Serializer):
    number= serializers.IntegerField()
    number_prefix = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    gender = serializers.IntegerField()
    dob = serializers.DateField()
    mobile = serializers.IntegerField()

    class Meta:
        model = Customer
        fields = "__all__"


class CollectionSerializer(serializers.Serializer):
    date= serializers.DateField()
    type = serializers.CharField()
    shift = serializers.CharField()
    quantity= serializers.DecimalField(max_digits=3,decimal_places=2)
    snf = serializers.DecimalField(max_digits=4,decimal_places=2)
    fat= serializers.DecimalField(max_digits=4,decimal_places=2)
    rate = serializers.DecimalField(max_digits=4,decimal_places=2)

    class Meta:
        model = Collection
        field ="__all__"




