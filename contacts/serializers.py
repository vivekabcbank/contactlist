from rest_framework import serializers
from .models import *


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ("country_code", "id", "first_name", "lastt_name", "phone_number", "conact_picture", "is_favourited",)
