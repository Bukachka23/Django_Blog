from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from django.conf import settings
from django.conf.urls.static import static


# A list of strings representing the full Python import paths to call to get the URLconfs for each installed application.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("core.urls", "core"), namespace="core")),
    path("users/", include(("users.urls", "users"), namespace="users")),
    path('social-auth/', include('social_django.urls', namespace='social')),
]

# A list of locations of the template source files, in search order.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
