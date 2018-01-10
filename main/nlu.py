from django.conf import settings
from requests.auth import HTTPBasicAuth
import requests


def compute_text_sentiment(text):
    """Compute the text's sentiment, using Watson NLU.

    :param url: the URL from which the article should be downloaded.
    """
    request_payload = {
        'text': text,
        'features': {
            'sentiment': {},
        },
    }

    response = requests.post(
        settings.NLU_URL, auth=HTTPBasicAuth(
            settings.NLU_USER, settings.NLU_PASSWORD
        ), json=request_payload
    )
    response_data = response.json()
    return (
        response_data['sentiment']['document']['label'],
        response_data['sentiment']['document']['score'],
    )
