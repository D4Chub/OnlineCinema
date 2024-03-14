from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from movies.views import MovieAPIList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movies.urls')),
    path('api/v1/movielist/', MovieAPIList.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
