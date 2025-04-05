from django.core.exceptions import ValidationError


class SingleCharacterValidator:
    def __init__(self, meassage=None):
        self.meassage = meassage or ('Значение не может состоять из одного символа')

    def __call__(self, value):
        if len(str(value)) == 1:
            raise ValidationError(self.meassage)


class MinCharacterValidator:
    "Валидатор минимальное количество символов"

    def __init__(self, min_value, meassage=None):
        self.min_value = min_value
        self.meassage = meassage or f'Значение не может быть меньше {self.min_value} символов.'

    def __call__(self, value):
        if self.min_value > len(value):
            raise ValidationError(
                f'Значение не может быть меньше {self.min_value} символов'
            )

    def deconstruct(self):
        return (
            'product.validation.MinCharacterValidator',
            (self.min_value,),
            {'meassage': self.meassage}
        )
