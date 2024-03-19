import requests

from utils.variables import HEADERS, URL

ENDPOINT = "vendas/"


def test_vendas_endpoint():
    url = URL + ENDPOINT

    def get_vendas():
        response = requests.get(url)
        assert response.status_code == 200
        pass

    def post_vendas():
        response = requests.post(
            url,
            json={
                "cnpj": "47270276000153",
                "telefone": "61996076351",
                "consultor": "PEDRO HENRIQUE",
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

    def update_vendas(id):
        response = requests.put(
            url,
            json={"id": id, "status": "CONCLUÍDO / PAGO", "tipo": "MIGRAÇÃO"},
            headers=HEADERS,
        )

        assert response.status_code == 200, response.text
        pass

    def delete_vendas(id):
        response = requests.put(url, json={"id": id}, headers=HEADERS)

        assert response.status_code == 200, response.text
        pass



    get_vendas()
    id = post_vendas()
    update_vendas(id)
    delete_vendas(id)
