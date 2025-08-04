import os
import tempfile
import shutil

import pytest
from django.conf import settings
from django.test import override_settings
from django.test import Client

from product.models import Product, Marketplace
from account.models import User


@pytest.fixture(scope="session", autouse=True)
def folder_test():
    os.makedirs(settings.MEDIA_ROOT_TESTS, exist_ok=True)
    TEMP_MEDIA_ROOT = tempfile.mkdtemp(
        dir=settings.MEDIA_ROOT_TESTS
        )
    with override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT):
        yield
    shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)


@pytest.fixture(scope="function")
def product(db):
    product = Product.objects.create(
        name='product_name',
        description='product_description'
    )
    yield product


@pytest.fixture(scope="function")
def marketplace(db):
    marketplace = Marketplace.objects.create(
        name='market'
    )
    yield marketplace


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
