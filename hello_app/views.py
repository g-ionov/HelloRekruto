from django.shortcuts import render


def hello_world(request):
    return render(request, 'index.html', {'name': request.GET.get('name'), 'message': request.GET.get('message')})
