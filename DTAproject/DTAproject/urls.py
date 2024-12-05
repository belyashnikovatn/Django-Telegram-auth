from django.contrib import admin
from django.urls import path

from app import views as app_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', app_view.index, name='homepage'),
    path('homepage/<int:tlg_id>/', app_view.user, name='homepage')
]
