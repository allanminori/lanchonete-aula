
def test_post_e_get_produto(client):
    
    response = client.post("/produtos", json={"código": "0001", "tipo": "Salgado X"})
    assert response.status_code == 200
    assert response.json()["código"] == "0001"

    response2 = client.get("/produtos/0001")
    assert response2.status_code == 200
    assert response2.json()["tipo"] == "Salgado X"


def test_get_produto_inexistente(client):
    
    response = client.get("/produtos/000")
    assert response.status_code == 404

    # resolver erro 422