import allure

from .base import BaseRequest

from ..urls import URLS

class ProductRequest(BaseRequest):

    def create(self, data):

        print(URLS["api"]["product"]["create"])
        response = self.post(
            url=URLS["api"]["product"]["create"],
            data=data
        )
        result = self.result_json(response)
        return result





