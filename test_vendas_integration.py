import requests

from utils.variables import HEADERS, URL

ENDPOINT = "vendas/"


def test_vendas_endpoint():
    url = URL + ENDPOINT

    def get_vendas():
        response = requests.get(url)
        assert response.status_code == 200
        pass

    get_vendas()