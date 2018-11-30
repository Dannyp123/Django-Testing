from django import forms


class AddForm(forms.Form):
    num1 = forms.FloatField()
    num2 = forms.FloatField()


class DoubleForm(forms.Form):
    num1 = forms.FloatField()


class TripleForm(forms.Form):
    num1 = forms.FloatField()


class EarningsForm(forms.Form):
    seat_a = forms.IntegerField()
    seat_b = forms.IntegerField()
    seat_c = forms.IntegerField()


class BothForm(forms.Form):
    input_1 = forms.BooleanField()
    input_2 = forms.BooleanField()
