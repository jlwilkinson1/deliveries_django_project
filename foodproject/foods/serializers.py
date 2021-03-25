from rest_framework import serializers
from .models import Offer, Restarantinfo

class RestarantinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restarantinfo
        fields = [
        "id",
        "rest_name",
        "rest_image",
        "is_closed", 
        "deliveries", 
        "pickup",
        "cuisines",
        "price",
        "phone",
        "address",
        "city",
        "zip_code",
        ]