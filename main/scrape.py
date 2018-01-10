from newspaper import Article


def scrape_article(url):
    """Scrape a news article's text.

    :param url: the URL from which the article should be downloaded.
    """
    article = Article(url=url)
    article.download()
    article.parse()
    return article.text
