from django.urls import include
from django.urls import re_path
from django.contrib import admin


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^selectable/', include('selectable.urls')),
    re_path(r'^', include('core.urls')),
]
