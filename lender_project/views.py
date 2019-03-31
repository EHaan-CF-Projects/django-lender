from django.shortcuts import render


def home_view(request):
    """Route to Home page."""
    return render(request, 'generic/home.html')