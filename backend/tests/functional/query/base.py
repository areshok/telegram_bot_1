import requests
import allure


class BaseRequest:

    @allure.step("Результат запроса")
    def result_json(self, response):
        status = self.status_code(response)
        try:
            body = self.body_json(response)
        except Exception:
            body = None
        return {
            "status": status,
            "body": body
        }

    @allure.step("Получаем код статуса")
    def status_code(self, response):
        return response.status_code

    @allure.step("Преобразуем тело ответа в json")
    def body_json(self, response):
        return response.json()

    @allure.step("отправляем Get запрос")
    def get(self, *args, **kwargs) -> requests.Response:
        return requests.get(*args, **kwargs)

    @allure.step("отправляем Post запрос")
    def post(self, *args, **kwargs) -> requests.Response:
        return requests.post(*args, **kwargs)









