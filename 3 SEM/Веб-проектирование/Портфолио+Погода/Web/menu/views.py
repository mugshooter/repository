from django.shortcuts import render
from django.http import HttpResponse

def menu(reqests):
    if reqests.method == "GET":
        return render(request=reqests, template_name='menu/index.html')
        