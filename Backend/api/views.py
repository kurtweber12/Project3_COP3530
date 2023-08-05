from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from api.utils import main, uniqueCountries
from api.serializers import DropDownSerializer, CountriesSerializer


# Create your views here.
class SearchResultView(APIView):
    # post request for our form on the front end
    def post(self, request):
        print(request.data)
        
        # convert all data types to make sure they are strings, 
        # to be properly used by the search and sort algos
        day = str(request.data.get('day'))
        month = str(request.data.get('month'))
        year = str(request.data.get('year'))
        country = str(request.data.get('location'))

        # main function is where we call our searching and sorting algos, it is inside utils.py
        linear_covid, lineary_time, ternary_covid, ternary_time = main(day, month, year, country)
        
        # serializer creates our data in a form to send as a response
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
        # uniqueCountries returns a set, we convert to a list and then serialize it to send as a response
        countries = uniqueCountries()
        countries_list = list(countries)
        
        serializer = DropDownSerializer(data={"unique_countries": countries_list})
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.validated_data, status=status.HTTP_200_OK)
