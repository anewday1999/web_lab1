from django.db import models
from django.db.models import fields
from rest_framework import serializers
from market.models import marketpost
from tutor.models import findtutorpost
from employee.models import employeepost

class marketpostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = marketpost
        fields = ('id', 'title', 'describe', 'address', 'contact', 'price', 'date_posted', 'date_outdate')
class tutorpostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = findtutorpost
        fields = ('id', 'title', 'main_content', 'subject', 'calendar', 'salary', 'contact', 'date_posted', 'date_outdate')
class employeepostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = employeepost
        fields = ('id', 'title', 'main_content', 'calendar', 'salary', 'contact', 'date_posted', 'date_outdate')