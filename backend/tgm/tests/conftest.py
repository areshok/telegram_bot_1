import os
import tempfile
import shutil

import pytest
from django.conf import settings
from django.test import override_settings
from django.test import Client

from account.models import User


@pytest.fixture(scope="function")
def auth_user(db):
    client = Client()
    User.objects.create_user(
            username='username',
            password='password'
        )
    client.login(
        username='username',
        password='password'
    )
    yield client


@pytest.fixture(scope="function")
def auth_admin(db):
    client = Client()
    admin = User.objects.create_superuser(
        username='adm_user',
        password='adm_pass'
    )
    client.force_login(admin)
    yield client


@pytest.fixture(scope="function")
def anon_user():
    return Client()


@pytest.fixture(scope="function")
def comment_product(db):
    return None