from django import forms
from django.core.exceptions import ValidationError

from .models import User


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username',]  # Поля, которые будут отображаться в форме

    def clean_password2(self):
        """
        Проверяем, совпадают ли пароли.
        """
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise ValidationError("Пароли не совпадают.")
        return password2

    def save(self, commit=True):
        """
        Сохраняем пользователя и устанавливаем пароль.
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user






