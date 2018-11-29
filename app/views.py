from django.shortcuts import render
from django.views import View


class Add(View):
    def get(self, request):
        try:
            num1 = float(request.GET.get('num1'))
            num2 = float(request.GET.get('num2'))
        except ValueError:
            return render(request, 'app/add.html')
        else:
            return render(request, 'app/add.html', {'answer': num1 + num2})


class Double(View):
    def get(self, request):
        try:
            num1 = float(request.GET.get('num1'))
        except ValueError:
            return render(request, 'app/double.html')
        else:
            return render(request, 'app/double.html', {'solution': num1 * 2})


class Triple(View):
    def get(self, request):
        try:
            num1 = float(request.GET.get('num1'))
        except ValueError:
            return render(request, 'app/triple.html')
        else:
            return render(request, 'app/triple.html', {'answer': num1 * 3})


class Earnings(View):
    def get(self, request):
        try:
            class_a = int(request.GET.get('a'))
            class_b = int(request.GET.get('b'))
            class_c = int(request.GET.get('c'))
        except ValueError:
            return render(request, 'app/earnings.html')
        else:
            return render(request, 'app/earnings.html', {
                'answer': class_a * 15 + class_b * 12 + class_c * 9,
            })

    # def get(self, request):
    #     try:

    #     except ValueError:
    #         return render(request, 'app/earnings.html')
    #     else:
    #         return render(request, 'app/earnings.html', {
    #             'answer': class_b * 12,
    #         })