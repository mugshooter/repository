from django.shortcuts import render

def exchange(reqests):
    return render(request=reqests, template_name='title/index.html')