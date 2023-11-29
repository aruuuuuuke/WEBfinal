from django.shortcuts import render
from rest_framework import generics
from .models import Group
from .serializers import GroupSerializer


class GroupAPIView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer