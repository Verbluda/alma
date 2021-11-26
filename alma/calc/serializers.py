from rest_framework import serializers
from calc.models import CalcData, Calculation


class CalcListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculation
        fields = ('id', 'date', 'calc_status')


class CalcCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalcData
        fields = ('date_start', 'date_fin', 'lag')


class CalcDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculation
        fields = '__all__'
