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
        return render(request, 'app/walk-or-drive.html')
