import allure
from django.urls import reverse


class TestCaseMarketingMassageUrl:
    "Тест кейс првоерки url связанных с моделью MarketingMessage"

    @allure.title("тест: проверка url marketing_message_list")
    def test_marketing_message_list_url(self):
        "тест: проверка url marketing_message_list"
        url = reverse("telegram:marketing_message_list")
        assert url == "/telegram/marketing-meassage/list/"

    @allure.title("тест: проверка url marketing_message_detail")
    def test_marketing_message_detail_url(self):
        "тест: проверка url marketing_message_detail"
        url = reverse("telegram:marketing_message_detail", kwargs={"pk": 1})
        assert url == "/telegram/markiting-message/1/"

    @allure.title("тест: проверка url marketing_message_create")
    def test_markiting_message_create_url(self):
        "тест: проверка url marketing_message_create"
        url = reverse("telegram:marketing_message_create")
        assert url == "/telegram/marketing-message/create/"

    @allure.title("тест: проверка url marketing_message_update")
    def test_markiting_message_update_url(self):
        "тест: проверка url marketing_message_update"
        url = reverse("telegram:marketing_message_update", kwargs={"pk": 1})
        assert url == "/telegram/markiting-message/1/update/"

    @allure.title("тест: проверка url markiting_message_delete")
    def test_markiting_message_delete_url(self):
        "тест: проверка url markiting_message_delete"
        url = reverse("telegram:markiting_message_delete", kwargs={"pk": 1})
        assert url == "/telegram/markiting-message/1/delete/"

    @allure.title("тест: првоерка url markiting_message_send")
    def test_markiting_message_send_url(self):
        "тест: првоерка url markiting_message_send"
        url = reverse("telegram:markiting_message_send", kwargs={"pk": 1})
        assert url == '/telegram/markiting-message/1/send/'

class TestCaseTelegramProfileUrl:
    ""

    def test_(self):
        assert 1 == 2

class TestCaseCommentProductUrl:
    "Тест кейс проверки url связанных с моделью CommentProduct"

    @allure.title("тест: проверка url comment_product_list")
    def test_comment_product_list_url(self):
        "тест: проверка url comment_product_list"
        url = reverse("telegram:comment_product_list")
        assert url == "/telegram/comment/"

    @allure.title("тест: проверка url comment_product_detail")
    def test_comment_product_detail_url(self):
        "тест: проверка url comment_product_detail"
        url = reverse("telegram:comment_product_detail", kwargs={"pk": 1})
        assert url == "/telegram/comment/1/"

    @allure.title("тест: проверка url comment_product_update")
    def test_comment_product_update_url(self):
        "тест: проверка url comment_product_update"
        url = reverse("telegram:comment_product_update", kwargs={"pk": 1})
        assert url == '/telegram/comment/1/update/'
