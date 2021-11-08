from django.urls import path
from crop.views import home_page
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', home_page)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
