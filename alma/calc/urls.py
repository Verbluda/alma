from django.urls import path
from calc.views import *


app_name = 'calc'
urlpatterns = [
    path('calc/create/', CalcCreateView.as_view()),
    path('all/', CalcListView.as_view()),
    path('calc<int:pk>/', CalcDetailView.as_view()),
]
