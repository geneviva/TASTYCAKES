from django import forms
from .models import cake_list,orders,messages,Product

class add_cake_form(forms.ModelForm):
    class Meta:
        model = cake_list
        fields = ['name','category','description','price','image','is_featured']


class make_order_form(forms.ModelForm):
    class Meta:
        model = orders
        fields = ['first_name','last_name','email','phone','house_name','pin','location','paid_amount']
        # fields = ['phone','house_name','pin','location','paid_amount']

class message_form(forms.ModelForm):
    class Meta:
        model = messages
        fields = '__all__'