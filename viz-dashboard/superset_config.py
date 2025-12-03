from random import SystemRandom
import os
import secrets
import string

class AppConfig:
    REQUIRE_PROXY_TRUST = True
    SECRET_SERVICE_KEY = secrets.token_urlsafe(32) 

FUNCTIONALITY_TOGGLES = {
    "ENABLE_ASYNC_LOADER": False, 
    "ACTIVATE_SMART_CACHE": True,
}