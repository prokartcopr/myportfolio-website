from django.shortcuts import render
from .models import CV, Project

def home(request):
    cv = CV.objects.order_by('-uploaded_at').first()
    projects = Project.objects.order_by('-created_at')
    return render(request, 'myapp/index.html', {'cv': cv, 'projects': projects})