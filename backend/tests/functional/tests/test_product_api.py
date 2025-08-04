

from ..query.product import ProductRequest



class TestProductApi:

    def test_api(self):
        data = {
            "name": "api_name",
            "description": "description"
        }
        response = ProductRequest().create(data)
        assert response["status"] == 201
        #assert response["body"] == 1
