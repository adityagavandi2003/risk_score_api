from rest_framework import serializers

class RiskInputSerializer(serializers.Serializer):
    purpose = serializers.CharField()
    data_sensitivity = serializers.CharField()
    region = serializers.CharField()
    processor_name = serializers.CharField()
