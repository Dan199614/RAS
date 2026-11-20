from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views
from .views import *

urlpatterns = [
                  path('', index, name='index'),
                  path('stream/', views.sse_stream, name='sse_stream'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
