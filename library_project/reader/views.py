from django.shortcuts import render
from .models import Reader


def reader_profile(request):
    reader = Reader.objects.get(email=request.user.email)
    return render(request, 'reader/reader_profile.html', {'reader': reader})
