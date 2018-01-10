from django.shortcuts import render

from .scrape import scrape_article
from .nlu import compute_text_sentiment


def index(request):
    context = {}
    if request.method == 'POST':
        url = request.POST['url']
        text, summary = scrape_article(url)
        context['results'] = True
        sentiment_overall, sentiment_score = compute_text_sentiment(text)
        context['sentiment_overall'] = sentiment_overall
        context['sentiment_score'] = sentiment_score
        context['text'] = text
        context['summary'] = text
        context['url'] = url
    return render(request, 'index.html', context)
