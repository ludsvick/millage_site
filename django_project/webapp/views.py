from django.shortcuts import render
from django.views.generic import FormView
from .models import County,Municipality, District

def index(request):
    County_results = County.objects.all()
    Municipality_results = Municipality.objects.all()
    District_results = District.objects.all()
    return render(request, 'webapp/home.html', {'County_results': County_results,
                                                'Municipality_results': Municipality_results,
                                                'District_results': District_results})
