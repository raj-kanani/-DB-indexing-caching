from django.urls import path
from .import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('caching/', views.caching),
    path('home/', views.home),
    path('get/', views.get_redis),
    path('show/<int:id>/', views.show_redis),
    path('custom/', cache_page(25)(views.custom_cache)),
    path('low/', views.low_level),
    path('memcache/', views.memcache),
]
