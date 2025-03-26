from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied


class AdminRequriedMixin(AccessMixin):
    "Доступ только админам"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            raise PermissionDenied('Доступ запрещен')
        return super().dispatch(request, *args, **kwargs)
