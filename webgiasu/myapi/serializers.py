from django.db import models
from django.db.models import fields
from rest_framework import serializers
from market.models import marketpost

class marketposstSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = marketpost
        fields = ('title', 'describe', 'address', 'contact', 'price', 'date_posted', 'date_outdate')