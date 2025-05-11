import unittest
import os

from dotenv import load_dotenv
from telegram import Bot
load_dotenv()




class TestTelegramBot(unittest.TestCase):
    "Тест кейс телеграм бота"

    @classmethod
    def setUpClass(cls):

        return super().setUpClass()

    def setUp(self):
        return super().setUp()

    async def test_bot_send_meassedge(self):
        self.fail('не сделанно')











