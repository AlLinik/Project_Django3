from django.shortcuts import render


def app_project(request):
    return render(request, 'app_project.html')
