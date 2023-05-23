from django import forms
from .models import HotelBill

class HotelBillForm(forms.ModelForm):
    class Meta:
        model = HotelBill
        fields = '__all__'
