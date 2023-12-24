from django.contrib import admin
from django.urls import path
from .views import index, ApartmentsUpdaterView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='home'),
    # path('updater/', ApartmentsUpdaterView.as_view(), name='update')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
