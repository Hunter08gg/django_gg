#from django.contrib import admin
#rom django.urls import path, include


#rlpatterns = [
#   path('admin/', admin.site.urls),
#]
from django.urls import path
from Страйкбольный_магазин.Страйкбольный_магазин.views import *
from Страйкбольный_магазин.django_site.urls import path

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("catalog/", catalog, name="catalog"),
   path("all-creaters/", api_get_all_creaters, name="api_all_creaters"),
]

