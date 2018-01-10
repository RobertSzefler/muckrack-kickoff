from newspaper import Article
import nltk


def scrape_article(url, summary=False):
    """Scrape a news article's text.

    :param url: the URL from which the article should be downloaded.
    """
    article = Article(url=url)
    article.download()
    # TODO handle occasional newspaper.article.ArticleExceptions below.
    article.parse()
    if summary:
        nltk.download('punkt')
        article.nlp()
        summary = article.summary
    else:
        summary = None
    return article.text, summary
