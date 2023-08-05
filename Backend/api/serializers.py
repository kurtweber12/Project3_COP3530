from rest_framework import serializers

# serializers prepare the data in a form where we can send as apart of the response from the view 
class DropDownSerializer(serializers.Serializer):
    unique_countries = serializers.ListField(child=serializers.CharField())


class CountriesSerializer(serializers.Serializer):
    linear_covid = serializers.ListField(child=serializers.CharField())
    linear_time = serializers.CharField()
    ternary_covid = serializers.ListField(child=serializers.CharField())
    ternary_time = serializers.CharField()