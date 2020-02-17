from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request, 'home.html')


def count(request):
    # collect the input
    fulltext = request.GET['fulltext']

    # split it in a list
    wordcount = fulltext.split()

    #Counts how many time each word appears
    word_dictionary = {}
    for word in wordcount:
        if word in word_dictionary:
            #increase
            word_dictionary[word] += 1
        else:
            #add to dictionary
            word_dictionary[word] = 1

    sortedwords =  sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse = True)

        

    return render(request, 'count.html',
         {'fulltext' : fulltext, 'count' : len(wordcount),
          'sortedwords': sortedwords})