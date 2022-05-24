from django.shortcuts import render
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from .models import *


# template fragment cache
def caching(request):
    return render(request, 'index.html')


# per view cache
@cache_page(25)
def custom_cache(request):
    return render(request, 'home.html')


# low level cache
# def low_level(request):
#     st = cache.get('movie', 'has_expired')
#     if st == 'has_expired':
#         # if we change value it must be update after 30 seconds.
#         cache.set('movie', 'KGF2', 30)
#         st = cache.get('movie')
#     return render(request, 'home.html', {'st': st})

# def low_level(request):
#     st = cache.get_or_set('roll', 150, 200)
#     return render(request, 'home.html', {'st': st})

def low_level(request):
    data = {'name': 'Raj', 'roll': 201}
    cache.set_many(data, 15)
    sv = cache.get_many(data)
    print(sv, '*************')
    return render(request, 'home.html', {'stu': sv})


# def low_level(request):
#     sv = cache.incr('roll', delta=4)
#     print(sv)
#     return render(request, 'home.html')

# def low_level(request):
#     cache.clear()
#     return render(request, 'home.html')

#  redis server
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def get_redis(filter_redis=None):
    if filter_redis:
        redis = Redis.objects.filter(name__contains=filter_redis)
    else:
        redis = Redis.objects.all()
        print(redis)
    return redis


def home(request):
    re = request.GET.get('re')
    if cache.get(re):
        print("DATA FROM CACHING")
        re = cache.get(re)
    else:
        if re:
            re = get_redis(re)
            cache.set(re, re)
        else:
            re = get_redis()
    return render(request, 'index.html', {'re': re})


def show_redis(request, id):
    if cache.get(id):
        print('data will come in cache')
        redis = cache.get(id)
    else:
        print('data will come  in database')
        redis = Redis.objects.get(id=id)
        cache.set(id, redis)
    return render(request, 'show.html', {'redis': redis})


def memcache(request):
    st = cache.get_or_set('mobile', 'vivo', 200)
    return render(request, 'memcache.html', {'st': st})
