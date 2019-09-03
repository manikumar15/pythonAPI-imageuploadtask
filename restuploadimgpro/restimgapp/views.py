from django.shortcuts import render

from .models import Student

from .serializers import StudentSerializer

from rest_framework.viewsets import ModelViewSet


class StudentViewSet(ModelViewSet):
	queryset=Student.objects.all().order_by('-sname')
	serializer_class=StudentSerializer

class DueViewSet(ModelViewSet):
	queryset=Student.objects.all().order_by('-sname').filter(task=False)
	serializer_class=StudentSerializer

class CompleteViewSet(ModelViewSet):
	queryset=Student.objects.all().order_by('-sname').filter(task=True)
	serializer_class=StudentSerializer
