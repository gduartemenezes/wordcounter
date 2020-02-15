from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordcount = fulltext.split()

    return render(request, 'count.html', {'fulltext' : fulltext, 'count' : len(wordcount) })