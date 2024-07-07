from django.shortcuts import render


def ships_list(request):
    template = 'ships/ships.html'
    return render(request, template)
