from unittest.mock import patch, sentinel

from main.nlu import compute_text_sentiment


@patch('main.nlu.requests')
@patch('main.nlu.HTTPBasicAuth')
@patch('main.nlu.settings')
def test_compute_text_sentiment(mock_settings, mock_auth, mock_requests):
    result = compute_text_sentiment(sentinel.text)

    expected_payload = {
        'text': sentinel.text,
        'features': {
            'sentiment': {},
        },
    }
    mock_auth.assert_called_once_with(
        mock_settings.NLU_USER, mock_settings.NLU_PASSWORD
    )
    mock_requests.post.assert_called_once_with(
        mock_settings.NLU_URL, auth=mock_auth.return_value,
        json=expected_payload
    )
    mock_data = mock_requests.post.return_value.json.return_value
    # TODO test accesses on mock_data and assert the returned value.
