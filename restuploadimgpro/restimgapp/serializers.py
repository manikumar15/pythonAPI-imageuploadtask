# from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
	image=serializers.ImageField(max_length=None,use_url=True)
	profile=serializers.FileField(max_length=None,use_url=True)
	class Meta:
		model = Student
		fields = '__all__'

