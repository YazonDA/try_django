from django.contrib import admin
from django.urls import include, path

from pages.views import HomeView, about_view


urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += [
    path('', HomeView, name='home'),
    path('about/', about_view),
]
