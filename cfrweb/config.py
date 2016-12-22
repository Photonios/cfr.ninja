import importlib
import os

settings_module = os.environ.get(
    'CFRWEB_SETTINGS_MODULE',
    'config.local'
)

settings = importlib.import_module(
    settings_module
)

__all__ = [
    'settings'
]
