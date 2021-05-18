from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def top_10_grades_view(request):
    #req.user
    return HttpResponse("<h1>Grades page </h1>")
