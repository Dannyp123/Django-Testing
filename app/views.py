from django.shortcuts import render
from django.views import View
from . import forms


class Add(View):
    def post(self, request):
        form = forms.AddForm(data=request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            return render(request, 'app/add.html', {
                'answer': num1 + num2,
                'addForm': form
            })
        else:
            return render(request, 'app/add.html', {'addForm': form})

    def get(self, request):
        return render(
            request,
            'app/add.html',
            {'addForm': forms.AddForm()},
        )


class Double(View):
    def post(self, request):
        form = forms.DoubleForm(data=request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            return render(
                request,
                'app/double.html',
                {
                    'solution': num1 * 2,
                    'doubleForm': form
                },
            )
        else:
            return render(request, 'app/double.html', {'doubleForm': form})

    def get(self, request):
        return render(
            request,
            'app/double.html',
            {'doubleForm': forms.DoubleForm()},
        )


class Triple(View):
    def post(self, request):
        form = forms.TripleForm(data=request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            num3 = form.cleaned_data['num3']
            return render(
                request,
                'app/triple.html',
                {
                    'answer': num1 * num2 * num3,
                    'tripleForm': form
                },
            )
        else:
            print('right here')
            return render(request, 'app/triple.html', {'tripleForm': form})

    def get(self, request):
        return render(
            request,
            'app/triple.html',
            {'tripleForm': forms.TripleForm()},
        )


class Earnings(View):
    def post(self, request):
        seat = forms.EarningsForm(data=request.POST)
        if seat.is_valid():
            seat_a = seat.cleaned_data['seat_a']
            seat_b = seat.cleaned_data['seat_b']
            seat_c = seat.cleaned_data['seat_c']
            return render(
                request, 'app/earnings.html', {
                    'answer': seat_a * 15 + seat_b * 12 + seat_c * 9,
                    'earningsForm': seat
                })
        else:
            return render(request, 'app/earnings.html', {'earningsForm': seat})

    def get(self, request):
        return render(
            request,
            'app/earnings.html',
            {'earningsForm': forms.EarningsForm()},
        )


class Both(View):
    def post(self, request):
        form = forms.BothForm(data=request.POST)
        if form.is_valid():
            input_1 = form.cleaned_data['input_1']
            input_2 = form.cleaned_data['input_2']
            if input_1 and input_2:
                return render(
                    request,
                    'app/both.html',
                    {
                        'answer': True,
                        'bothForm': form
                    },
                )
            else:
                return render(request, 'app/both.html', {
                    'answer': False,
                })
        else:
            return render(request, 'app/both.html', {'bothForm': form})

    def get(self, request):
        return render(
            request,
            'app/earnings.html',
            {'bothForm': forms.BothForm()},
        )


class WalkOrDrive(View):
    def post(self, request):
        form = forms.WalkOrDriveForm(data=request.POST)
        if form.is_valid():
            distance_input = form.cleaned_data['distance_input']
            is_nice_weather_input = form.cleaned_data['is_nice_weather_input']
            if distance_input <= 0.25 and is_nice_weather_input:
                return render(request, 'app/walk-or-drive.html', {
                    'answer': 'walk',
                    'walk_or_driveForm': form
                })
            else:
                return render(request, 'app/walk-or-drive.html',
                              {'answer': 'drive'})
        else:
            return render(request, 'app/walk-or-drive.html',
                          {'walk_or_driveForm': form})

    def get(self, request):
        return render(
            request,
            'app/walk-or-drive.html',
            {'walk_or_driveForm': forms.WalkOrDriveForm()},
        )


class HowPopulated(View):
    def post(self, request):
        form = forms.HowPopulate(data=request.POST)
        if form.is_valid():
            population_input = form.cleaned_data['population_input']
            land_area_input = form.cleaned_data['land_area_input']
            if population_input / land_area_input > 100:
                return render(
                    request,
                    'app/how-populated.html',
                    {
                        'answer': 'Densely Populated',
                        'how_populatedForm': form
                    },
                )
            else:
                return render(request, 'app/how-populated.html',
                              {'answer': 'Sparsely Populated'})
        else:
            return render(request, 'app/how-populated.html',
                          {'how_populatedForm': form})

    def get(self, request):
        return render(
            request,
            'app/how-populated.html',
            {'walk_or_driveForm': forms.HowPopulate()},
        )


class GoldStars(View):
    def get(self, request):
        form = forms.GoldStars(data=request.GET)
        if form.is_valid():
            score_input = form.cleaned_data['score_input']
            if score_input < 1000:
                return render(request, 'app/gold-stars.html', {'answer': '*'})
            elif score_input < 5000:
                return render(request, 'app/gold-stars.html', {'answer': '**'})
            elif score_input < 8000:
                return render(request, 'app/gold-stars.html',
                              {'answer': '***'})
            elif score_input < 10000:
                return render(request, 'app/gold-stars.html',
                              {'answer': '****'})
            elif score_input >= 10000:
                return render(request, 'app/gold-stars.html',
                              {'answer': '*****'})
        else:
            return render(request, 'app/gold-stars.html')


class HowManyPoints(View):
    def get(self, request):
        form = forms.HowManyPoints(data=request.GET)
        if form.is_valid():
            points_input = form.cleaned_data['points_input']
            if points_input == 'extra kick':
                return render(
                    request,
                    'app/points.html',
                    {'answer': 1},
                )
            elif points_input == 'extra conv':
                return render(
                    request,
                    'app/points.html',
                    {'answer': 2},
                )
            elif points_input == 'safety':
                return render(
                    request,
                    'app/points.html',
                    {'answer': 2},
                )
            elif points_input == 'fg':
                return render(
                    request,
                    'app/points.html',
                    {'answer': 3},
                )
            elif points_input == 'td':
                return render(
                    request,
                    'app/points.html',
                    {'answer': 6},
                )
        else:
            return render(request, 'app/points.html')
