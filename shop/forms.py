from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from shop.models import Order


class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Make the Order'))

    class Meta:
        model = Order
        fields = ['phone', 'email', 'address']

