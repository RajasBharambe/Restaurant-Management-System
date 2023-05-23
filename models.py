from django.db import models

class HotelBill(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    cindate = models.DateField()
    coutdate = models.DateField()
    rno = models.IntegerField()
    s = models.IntegerField(default=0)
    t = models.IntegerField(default=0)
    p = models.IntegerField(default=0)
    r = models.IntegerField(default=0)
    rt = models.IntegerField(default=0)

    class Meta:
        app_label = 'hotel'