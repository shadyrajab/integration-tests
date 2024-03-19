import requests

from utils.variables import HEADERS, URL

ENDPOINT = "migracoes/"


def test_migracoes_endpoint():
    url = URL + ENDPOINT

    def get_migracoes():
        response = requests.get(url)

        assert response.status_code == 200
        pass

    def post_migracoes():
        response = requests.post(
            url=URL + "vendas/",
            json={
                "cnpj": "47270276000153",
                "telefone": "61996076351",
                "consultor": "FLAVIO HENRIQUE",
                "data": "19-03-2024",
                "gestor": "INTEGRATION TEST",
                "preco": 13.99,
                "plano": "SMART EMPRESAS 6 GB",
                "volume": 5,
                "equipe": "FREECEL",
                "tipo": "AVANÇADA",
                "ja_cliente": False,
                "email": "shadyrajaab@gmail.com",
                "ddd": "61",
                "status": "CONCLUÍDO",
                "numero_pedido": "AHSHDJAHSHDJS",
            },
            headers=HEADERS,
        )

        assert response.status_code == 200, response.text
        return response.json()["id"]

    def update_migracoes(id):
        response = requests.put(
            url, json={"id": id, "status": "CONCLUÍDO / PAGO"}, headers=HEADERS
        )

        assert response.status_code == 200
        pass

    def delete_migracoes(id):
        response = requests.delete(URL + "vendas/", json={"id": id}, headers=HEADERS)
        assert response.status_code == 200
        pass

    get_migracoes()
    id = post_migracoes()
    update_migracoes(id)
    delete_migracoes(id)
