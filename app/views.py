from django.shortcuts import render
from django.views import View
from . import forms


class Add(View):
    def get(self, request):
        form = forms.AddForm(data=request.GET)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            return render(request, 'app/add.html', {'answer': num1 + num2})
        else:
            return render(request, 'app/add.html')


class Double(View):
    def get(self, request):
        form = forms.DoubleForm(data=request.GET)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            return render(request, 'app/double.html', {'solution': num1 * 2})
        else:
            return render(request, 'app/double.html')


class Triple(View):
    def get(self, request):
        form = forms.TripleForm(data=request.GET)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            return render(request, 'app/triple.html', {'answer': num1 * 3})
        else:
            return render(request, 'app/triple.html')


class Earnings(View):
    def get(self, request):
        seat = forms.EarningsForm(data=request.GET)
        if seat.is_valid():
            seat_a = seat.cleaned_data['seat_a']
            seat_b = seat.cleaned_data['seat_b']
            seat_c = seat.cleaned_data['seat_c']
            return render(request, 'app/earnings.html', {
                'answer': seat_a * 15 + seat_b * 12 + seat_c * 9,
            })
        else:
            return render(request, 'app/earnings.html')


class Both(View):
    def get(self, request):
        form = forms.BothForm(data=request.GET)
        if form.is_valid():
            input_1 = form.cleaned_data['input_1']
            input_2 = form.cleaned_data['input_2']
            if input_1 and input_2:
                return render(request, 'app/both.html', {'answer': True})
            else:
                return render(request, 'app/both.html', {'answer': False})
        else:
            return render(request, 'app/both.html')


class WalkOrDrive(View):
    def get(self, request):
        form = forms.WalkOrDrive(data=request.GET)
        if form.is_valid():
            distance_input = form.cleaned_data['distance_input']
            is_nice_weather_input = form.cleaned_data['is_nice_weather_input']
            if distance_input <= 0.25 and is_nice_weather_input:
                return render(request, 'app/walk-or-drive.html',
                              {'answer': 'walk'})
            else:
                return render(request, 'app/walk-or-drive.html',
                              {'answer': 'drive'})
        else:
            return render(request, 'app/walk-or-drive.html')


class HowPopulated(View):
    def get(self, request):
        form = forms.HowPopulate(data=request.GET)
        if form.is_valid():
            population_input = form.cleaned_data['population_input']
            land_area_input = form.cleaned_data['land_area_input']
            if population_input / land_area_input > 100:
                return render(request, 'app/how-populated',
                              {'answer': 'Densely Populated'})
            else:
                return render(request, 'app/how-populated',
                              {'answer': 'Sparsely Populated'})
        else:
            return render(request, 'app/how-populated')