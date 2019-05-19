from django.urls import path, re_path
from . import views

urlpatterns = [
    # Catch-all path to spit anything to lead.
    re_path(r'^get_clients/', views.get_clients, name='get_clients'),
    re_path(r'^create_feature/', views.create_feature, name='create_feature'),
]
