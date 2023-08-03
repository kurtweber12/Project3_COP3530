from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class SearchResultView(APIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK)
    
    def post(self, request):
        print(request.data)
        return Response(status=status.HTTP_202_ACCEPTED)
