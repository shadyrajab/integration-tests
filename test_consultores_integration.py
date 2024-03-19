import requests

from utils.variables import HEADERS, URL

ENDPOINT = "consultores/"

def test_consultores_endpoint():
    url = URL + ENDPOINT

    def get_consultores():
        response = requests.get(url)
        assert response.status_code == 200
        pass

    def post_consultores():
        response = requests.post(
            url,
            json={
                "name": "INTEGRATION",
                "vinculo": "FREECEL",
                "cargo": "SUPERVISOR",
            },
            headers=HEADERS,
        )

        assert response.status_code == 200
        return response.json()["id"]

    def update_consultores(id):
        response = requests.put(
            url, json={"id": id, "vinculo": "FREECEL"}, headers=HEADERS
        )

        assert response.status_code == 200
        pass

    def delete_consultores(id):
        response = requests.delete(url, json={"id": id}, headers=HEADERS)
        assert response.status_code == 200
        pass

    get_consultores()
    id = post_consultores()
    update_consultores(id)
    delete_consultores(id)
