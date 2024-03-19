import requests

from utils.variables import HEADERS, URL

ENDPOINT = "produtos/"


def test_produtos_endpoint():
    url = URL + ENDPOINT

    def get_produtos():
        response = requests.get(url)
        assert response.status_code == 200
        pass

    def post_produtos():
        response = requests.post(
            url,
            json={
                "nome": "INTEGRATION TEST",
                "preco": 39.99,
            },
            headers=HEADERS,
        )

        assert response.status_code == 200
        return response.json()["id"]

    def update_produtos(id):
        response = requests.put(
            url,
            json={
                "id": id,
                "nome": "Integration Test",
                "preco": 29.99,
            },
            headers=HEADERS,
        )

        assert response.status_code == 200
        pass

    def delete_produtos(id):
        response = requests.delete(url, json={"id": id}, headers=HEADERS)
        assert response.status_code == 200
        pass


    get_produtos()
    id = post_produtos()
    update_produtos(id)
    delete_produtos(id)