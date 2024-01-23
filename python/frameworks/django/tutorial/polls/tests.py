from django.test import TestCase, Client

# Create your tests here.
def test_index():
    client = Client()
    response = client.get('/polls/')
    assert response.status_code == 200
