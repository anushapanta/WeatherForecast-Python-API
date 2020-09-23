from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html') #returns the index.html template
