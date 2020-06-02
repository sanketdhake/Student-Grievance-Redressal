from django.shortcuts import render

#sgr_views

def home(request):
	return render(request, 'home.html')