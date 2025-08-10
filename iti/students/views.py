from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def students_list(request):
    # return HttpResponse("students_list")
    return render(request, 'index.html')