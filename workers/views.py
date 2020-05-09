from django.shortcuts import render
from django.http import HttpResponse
from .models import Workers
from django.shortcuts import render, redirect
from django.http import HttpResponse

def workers(request):
    workers = Workers.objects.order_by('id')
    return render(request, 'workers/show_workers.html', {'workers': workers})


