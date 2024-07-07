from django.shortcuts import render

# Create your views here.


def homepage(request):
    template = 'homepage.html'
    return render(request, template)
