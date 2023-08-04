from rest_framework import serializers

class DropDownSerializer(serializers.Serializer):
    unique_countries = serializers.ListField(child=serializers.CharField())


class CountriesSerializer(serializers.Serializer):
    linear_covid = serializers.ListField(child=serializers.CharField())
    linear_time = serializers.CharField()
    ternary_covid = serializers.ListField(child=serializers.CharField())
    ternary_covid = serializers.CharField()