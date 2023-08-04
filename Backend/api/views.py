from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from api.utils import main, uniqueCountries
import json

# Create your views here.
class SearchResultView(APIView):
    def get(self, request):
        #main()
        return Response(status=status.HTTP_200_OK)
    
    def post(self, request):
        print(request.data)
        # print(request.data.get('day'))
        day = request.data.get('day')
        month = request.data.get('month')
        year = request.data.get('year')
        country = request.data.get('country')
        main(day, month, year, country)
        return Response(status=status.HTTP_202_ACCEPTED)
    

class DropDownView(APIView):
    def get(self, request):
        countries = uniqueCountries()
        countries_list = list(countries)
        #print(countries_list[1])
        json_res = json.dumps({"unique_countries" : countries_list})
        print(json_res)
        return Response(data=json_res, status=status.HTTP_200_OK)
