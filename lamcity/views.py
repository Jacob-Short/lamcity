from django.shortcuts import render

def index_view(request):
    context = None
    return render(request, 'index.html', context)
