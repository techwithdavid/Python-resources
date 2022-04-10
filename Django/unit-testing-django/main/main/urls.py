from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('hello/', include('hello_app.urls')),
    path('admin/', admin.site.urls),
]