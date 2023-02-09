from django.shortcuts import render
from django.http import HttpResponse
from .models import TestModel

# Create your views here.
# def home(request):
#     return HttpResponse('S T A R T H E R E')

def test_path(request):
    tests = TestModel.objects.all()
    context = {
        'tests': tests
    }
    return render(request, 'test_content.html', context=context)