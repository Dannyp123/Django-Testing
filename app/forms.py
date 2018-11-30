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
    input_1 = forms.BooleanField(required=False)
    input_2 = forms.BooleanField(required=False)


class WalkOrDrive(forms.Form):
    distance_input = forms.FloatField(min_value=0)
    is_nice_weather_input = forms.BooleanField(required=False)