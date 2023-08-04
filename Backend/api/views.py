from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from api.utils import main, uniqueCountries
from api.serializers import DropDownSerializer, CountriesSerializer
import json


# Create your views here.
class SearchResultView(APIView):
    def get(self, request):
        #main()
        return Response(status=status.HTTP_200_OK)
    
    def post(self, request):
        print(request.data)
        # print(request.data.get('day'))
        day = str(request.data.get('day'))
        month = str(request.data.get('month'))
        year = str(request.data.get('year'))
        country = str(request.data.get('location'))
        linear_covid, lineary_time, ternary_covid, ternary_time = main(day, month, year, country)
        serializer = CountriesSerializer(data={
            "linear_covid": linear_covid,
            "linear_time": lineary_time,
            "ternary_covid": ternary_covid,
            "ternary_time": ternary_time
        })
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.validated_data, status=status.HTTP_202_ACCEPTED)
    

class DropDownView(APIView):
    def get(self, request):
        countries = uniqueCountries()
        countries_list = list(countries)
        
        # json_res = json.dumps({"unique" : countries_list})
        # print(json_res)
        serializer = DropDownSerializer(data={"unique_countries": countries_list})
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.validated_data, status=status.HTTP_200_OK)
