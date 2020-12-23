from django.contrib import admin
from django.urls import (path, re_path, include)
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
]
