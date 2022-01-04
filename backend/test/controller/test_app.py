from test import BaseTestCase


class SearchEndpointTestCase(BaseTestCase):

    def test_endpoint_status_can_be_checked(self):
        response = self.client.get('/search?q=Cotton Twill Cap')

        assert response.status_code == 200

        for item in response.json:
            assert 'thumbnail' in item
            assert 'product_title' in item
            assert 'stock' in item
            assert 'currency' in item

    def test_it_returns_empty_when_no_query(self):
        response = self.client.get('/search')

        assert response.status_code == 200
