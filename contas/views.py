from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def home(request):
    now = datetime.datetime.now()
    html = now
    return render(request, 'contas/home.html')