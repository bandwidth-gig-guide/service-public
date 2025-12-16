import os
import json
import hashlib
from typing import Callable, Any
import redis


REDIS_HOST = os.getenv("REDIS_HOST", "")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
CACHE_DISABLED = REDIS_HOST == ""

DEFAULT_TTL: int = 300

_redis = None

def _init_redis():
    global _redis
    if CACHE_DISABLED:
        return

    try:
        _redis = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            decode_responses=True,
            socket_connect_timeout=1,
            socket_timeout=1,
        )
        _redis.ping()
    except Exception:
        _redis = None
        print("Redis Unavailable. Cache Disabled")

_init_redis()


def _hash(value: str) -> str:
    return hashlib.sha1(value.encode("utf-8")).hexdigest()


def make_key(base: str, **params) -> str:
    if not params:
        return base

    normalized = "|".join(
        f"{key}={sorted(value) if isinstance(value, list) else value}"
        for key, value in sorted(params.items())
        if value is not None
    )

    return f"{base}:{_hash(normalized)}"


def cache_wrap( key: str, fetch_fn: Callable[[], Any], ttl: int = DEFAULT_TTL, ):
    if CACHE_DISABLED or _redis is None:
        return fetch_fn()

    try:
        cached = _redis.get(key)
        if cached is not None:
            print("Cache hit!")
            return json.loads(cached)

        data = fetch_fn()
        _redis.setex(key, ttl, json.dumps(data, default=str))
        return data

    except Exception:
        return fetch_fn()
