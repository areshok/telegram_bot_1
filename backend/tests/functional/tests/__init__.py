import allure

from ..query.product import ProductRequest




class TestCaseProductAPI:


    def test_product_create_api(self):
        data = {
            "name": "api_test",
            "deacription": "description_api"
        }
        response = ProductRequest().create(data)

        assert response["status"] == 201
        assert response["body"] == 1