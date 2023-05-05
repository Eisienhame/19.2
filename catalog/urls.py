from django.urls import path
from catalog.views import take_contact, take_homepage
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [

    path('', take_homepage),
    path('', take_contact),
]
