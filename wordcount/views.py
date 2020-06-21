# returns an http as response
from django.http import HttpResponse
# render redirects a request to home.html inside the template folder
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext'] # pulls the parameter (text after ?fulltext) and assigns it to variable full text

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            # Increase here
            worddictionary[word] += 1
        else:
            # Add to the dictionary
            worddictionary[word] = 1

    # key = operator.itemgetter(1) is to sort the values according to count
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    # worddictionary.items() converts the dictionary into a list
    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})

def about(request):
    return render(request, 'about.html')
