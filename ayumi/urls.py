from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('professors.urls')),
    path("", include("allauth.urls")),
]
handler404 = 'professors.views.error_404_view'