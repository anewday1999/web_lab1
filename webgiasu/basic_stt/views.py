from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'home.html', {
        'nav':'home'})

def about(request):
    return render(request, 'about.html', {
        'nav':'about'})

def report(request):
    return render(request, 'report.html', {
        'nav':'report'})