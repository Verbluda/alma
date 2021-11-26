from django.db import models


class Calculation(models.Model):
    date = models.DateField(auto_now=False)
    liquid = models.DecimalField(max_digits=100, decimal_places=2)
    oil = models.DecimalField(max_digits=100, decimal_places=2)
    water = models.DecimalField(max_digits=100, decimal_places=2)
    wct = models.DecimalField(max_digits=100, decimal_places=2)
    STATUS_TYPE = (
        (1, 'завершен'),
        (2, 'идет расчет'),
        (3, 'в очереди'),
    )
    calc_status = models.IntegerField(choices=STATUS_TYPE)
    calc_duration = models.DurationField()


class CalcData(models.Model):
    date_start = models.DateField(auto_now=False)
    date_fin = models.DateField(auto_now=False)
    lag = models.IntegerField()
