

class BaseForm:
    data = {}

    @classmethod
    def get_data(cls, param):
        return cls.data.get(param)

class UserForm(BaseForm):
    data = {
        "correct": {"username": "admin", "password": "Areshok1980"},
        "uncorrect": {}
    }


class ProductForm:
    data = {
        "correct": {},
        "uncorrect": {}
    }


class MarketplaceForm:
    data = {
        "correct": {},
        "uncorrect": {}
    }



