from django.shortcuts import render
from .models import CV

def home(request):
    # Get the latest CV or None if no CV exists
    cv = CV.objects.order_by('-uploaded_at').first()
    return render(request, 'myapp/index.html', {'cv': cv})