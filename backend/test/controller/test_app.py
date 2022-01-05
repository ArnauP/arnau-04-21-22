from test import BaseTestCase


class SearchEndpointTestCase(BaseTestCase):
    def test_endpoint_returns_query_results(self) -> None:
        response = self.client.get('/search?q=Cotton Twill Cap')

        assert response.status_code == 200

        for item in response.json:
            assert '_id' in item
            assert 'thumbnail' in item
            assert 'product_title' in item
            assert 'stock' in item
            assert 'price' in item
            assert 'currency' in item

    def test_bad_request_when_no_query(self) -> None:
        response = self.client.get('/search')

        assert response.status_code == 400

    def test_alive(self) -> None:
        response = self.client.get('/')

        assert response.status_code == 200
