from unittest.mock import call, patch, sentinel

from main.scrape import scrape_article


@patch('main.scrape.Article')
@patch('main.scrape.nltk')
def test_scrape_article_no_summary(mock_nltk, mock_article_cls):
    result = scrape_article(sentinel.url)
    mock_article_cls.assert_called_once_with(url=sentinel.url)
    mock_article = mock_article_cls.return_value
    mock_article.assert_has_calls([call.download(), call.parse()])
    mock_nltk.download.assert_not_called()
    mock_article.nlp.assert_not_called()
    assert result == (mock_article.text, None)


@patch('main.scrape.Article')
@patch('main.scrape.nltk')
def test_scrape_article_with_summary(mock_nltk, mock_article_cls):
    result = scrape_article(sentinel.url, summary=True)
    mock_article_cls.assert_called_once_with(url=sentinel.url)
    mock_article = mock_article_cls.return_value
    mock_nltk.download.assert_called_once_with('punkt')
    mock_article.assert_has_calls([call.download(), call.parse(), call.nlp()])
    assert result == (mock_article.text, mock_article.summary)
