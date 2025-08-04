import allure


class TestCaseProductModel:

    @allure.title(
            """тест: проверка атоматического создание
        qrcode при создании объекта Product"""
    )
    @allure.description(
        """
        Должен создавать qrcode автоматически при создании объекта в дб,
        Проверяется есть ли в поле qrcode, путь до файла
        """
    )
    def test_signal_create_qrcode(self, product):
        """тест: проверка атоматического создание
        qrcode при создании объекта Product"""
        assert product.qrcode == f'qrcode/{product.id}_{product.name}_qrcode.png'
