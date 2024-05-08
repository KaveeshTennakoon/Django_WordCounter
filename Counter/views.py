from django.shortcuts import render

def WordCounting(request):
    no_of_words = 0
    if request.method == "POST":
        text = request.POST.get('words')
        no_of_words = len(text.split())
    return render(request, 'index.html', {'word_count' : no_of_words})
