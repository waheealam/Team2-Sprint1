from django import forms
from .models import Order,User,Profile

class DateInput(forms.DateInput):
    input_type = 'date'

class OrderForm(forms.ModelForm):
   class Meta:
       model = Order
       fields = ('aptID', 'ordDescription', 'created_date', 'ordPriority', 'ordStatus', 'ordProbType')
       widgets = {
           'created_date': DateInput()
       }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email',)