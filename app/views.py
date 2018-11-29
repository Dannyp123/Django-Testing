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
            number1 = float(request.GET.get('number1'))
        except ValueError:
            return render(request, 'app/double.html', {'solution': solution})
        else:
            solution = number1 * 2
            return render(request, 'app/double.html')


class Triple(View):
    def get(self, request):
        num1 = request.GET.get('num1')
        num2 = request.GET.get("num2")
        num3 = request.GET.get("num3")
