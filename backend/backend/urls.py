
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/product/')),
    path('product/', include('product.urls')),
    path('account/', include('account.urls')),
    path('telegram/', include('tgm.urls')),
    path("api/v1/", include("api.urls"))
]
