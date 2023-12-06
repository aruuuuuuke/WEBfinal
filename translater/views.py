from django.shortcuts import render
from rest_framework import generics
from .models import Group
from .serializers import GroupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class GroupAPIView(APIView):
    def post(self, request):
        return Response({'name':'food'})


# class GroupAPIView(generics.ListAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
