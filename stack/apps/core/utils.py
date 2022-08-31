from core.ratelimit import limits, RateLimitException
from backoff import on_exception, expo

import requests

MINUTES_IN_SECONDS = 60
CALLS_PER_MINUTES_IN_SECONDS = 5

DAY_IN_SECONDS = 86400
CALLS_PER_DAY = 100

"""Calling some decorators function for limit checking"""
@on_exception(expo, RateLimitException, max_tries=2)
@limits(calls=CALLS_PER_MINUTES_IN_SECONDS, period=MINUTES_IN_SECONDS)
@limits(calls=DAY_IN_SECONDS, period=CALLS_PER_DAY)
def call_api(url, headers, payload ):
    response = requests.request("GET", url, headers=headers, data=payload)
    return response