from rest_framework import generics
from calc.serializers import CalcCreateSerializer, CalcListSerializer, CalcDetailSerializer
from calc.models import Calculation
from calc.kernel import *


class CalcCreateView(generics.CreateAPIView):
    serializer_class = CalcDetailSerializer

    def perform_create(self, serializer):
        kernel.main(serializer)


class CalcListView(generics.ListAPIView):
    serializer_class = CalcListSerializer
    queryset = Calculation.objects.order_by('-date')[:10]


class CalcDetailView(generics.RetrieveAPIView):
    serializer_class = CalcDetailSerializer
    queryset = Calculation.objects.all()
