from utils.api_client import APIClient


def test_public_api_example(request_context):
    api = APIClient(request_context)

    response = api.get("https://reqres.in/api/users", params={"page": 2})
    assert response.ok

    data = response.json()
    assert data["page"] == 2
    assert len(data["data"]) > 0
