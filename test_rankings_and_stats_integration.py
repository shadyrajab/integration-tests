import requests

from utils.variables import HEADERS, URL

ENDPOINT_RANKINGS = "rankings/"
ENDPOINT_STATS = "stats/"


def test_rankings_endpoint():
    url = URL + ENDPOINT_RANKINGS

    def get_rankings():
        response = requests.get(url, params={"ano": 2023, "mes": "Janeiro"})

        assert response.status_code == 200
        pass

    get_rankings()


def test_stats_endpoint():
    url = URL + ENDPOINT_RANKINGS

    def get_stats():
        response = requests.get(url, params={"ano": 2023, "mes": "Janeiro"})

        assert response.status_code == 200
        pass

    get_stats()
