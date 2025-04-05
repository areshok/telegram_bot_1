from django.core.exceptions import ValidationError



class SingleCharacterValidator:
    def __init__(self, meassage=None):
        self.meassage = meassage or ('Значение не может состоять из одного символа')


    def __call__(self, value):
        if len(str(value)) == 1:
            raise ValidationError(self.meassage)


class MinCharacterValidator:
    def __init__(self, min_value, meassage=None):
        self.min_value = min_value
        self.meassage = meassage

    def __call__(self, value):
        if self.min_value > len(value):
            raise ValidationError(
                f'Значение не может быть меньше {self.min_value} символов'
            )

