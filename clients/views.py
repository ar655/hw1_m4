from django.shortcuts import render

from .models import Client



def clients_list(request):
    context = {}
    clients_lisst = Client.objects.all()
    context['clients_lisst'] = clients_lisst
    return render(request,'clients.html',context)