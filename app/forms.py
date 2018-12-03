from django import forms


class AddForm(forms.Form):
    num1 = forms.FloatField(label='Number 1')
    num2 = forms.FloatField(label='Number 2')


class DoubleForm(forms.Form):
    num1 = forms.FloatField(label='Number 1')


class TripleForm(forms.Form):
    num1 = forms.FloatField(label='Number 1')
    num2 = forms.FloatField(label='Number 2')
    num3 = forms.FloatField(label='Number 3')


class EarningsForm(forms.Form):
    seat_a = forms.IntegerField(label='Number 1')
    seat_b = forms.IntegerField(label='Number 2')
    seat_c = forms.IntegerField(label='Number 2')


class BothForm(forms.Form):
    input_1 = forms.BooleanField(required=False)
    input_2 = forms.BooleanField(required=False)


class WalkOrDrive(forms.Form):
    distance_input = forms.FloatField(min_value=0)
    is_nice_weather_input = forms.BooleanField(required=False)


class HowPopulate(forms.Form):
    population_input = forms.FloatField(min_value=0)
    land_area_input = forms.FloatField(min_value=0)


class GoldStars(forms.Form):
    score_input = forms.IntegerField()


class HowManyPoints(forms.Form):
    points_input = forms.CharField()