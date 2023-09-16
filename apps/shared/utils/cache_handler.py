from django.core.cache import cache


def set_and_extend_cache(key, value, ttl):
    cache.set(key, value, ttl)
    cache.expire(key, timeout=ttl)
