from rest_framework import serializers

from .models import contcatagory,contentelement


class Inforserializer(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    class Meta:
        model=contentelement
        fields = [

            'id',
            'title',
            'content'
        ]

