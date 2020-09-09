from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    texts = request.POST.get('text', 'default')
    #Check checkboxvalue
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')

    if removepunc == 'on':
        analyzed = ''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        for char in texts:
            if char not in punctuations:
                analyzed = analyzed + char
        texts = analyzed
        params = {'purpose': 'Removing Punctuation', 'analyzed_text': texts}

        # return render(request, 'analyze.html', params)


    if fullcaps == 'on':
        analyzed = ""

        for char in texts:
            analyzed = analyzed + char.upper()
        texts = analyzed
        params = {'purpose': 'Capitalization', 'analyzed_text': texts}

        # return render(request, 'analyze.html', params)


    if newlineremover == 'on':
        analyzed = ""

        for char in texts:
            if char != '\n' and char != "\r":
                analyzed = analyzed + char
        texts = analyzed
        params = {'purpose': 'Removing New Line', 'analyzed_text': texts}
        # return render(request, 'analyze.html', params)


    if spaceremover == 'on':
        analyzed = ""

        for index, char in enumerate(texts):
            if not (texts[index] == " " and texts[index + 1] == " "):
                analyzed = analyzed + char
        texts = analyzed
        params = {'purpose': 'Removing extra space', 'analyzed_text': texts}

        # return render(request, 'analyze.html', params)


    if (removepunc == 'on' or fullcaps == 'on' or newlineremover == 'on' or spaceremover == 'on'):
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error!! Try again!")

def about(request):
    return render(request, 'about.html')
#     <!--  {% url 'name' %} is used to link html file  -->


def contact(request):
    return render(request, 'contact.html')
