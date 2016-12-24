import collections
import os
from urllib.parse import urlparse

# Enable/disable debug mode
DEBUG = False

# Path to the root of the repo and the cfrweb directory
ROOT_DIR = os.path.join(os.path.dirname(__file__), '..')
PROJECT_DIR = os.path.join(os.path.dirname(__file__), '../cfrweb')

# Directory from which static files are served
STATIC_FILES_DIR = os.path.join(PROJECT_DIR, 'assets')

# Amount of seconds to cache resources of
# the specified mime types
CACHE_TIMEOUT = collections.OrderedDict([
    ('image/*', 604800),
    ('text/*', 300),
    ('*', 300)
])

# Name of the website
SITE_NAME = 'CFR Ninja'

# Jinja2 template configuration
TEMPLATES_DIR = os.path.join(ROOT_DIR, 'cfrweb/templates')
TEMPLATES_DEFAULT_CONTEXT = {
    'meta': {
        'title': SITE_NAME,
        'page': None,
        'description': 'Real-time updates on trains in Romania.',
        'keywords': 'CFR Romania real-time updates train'
    }
}

# Redis server to use for caching
REDIS_URL = urlparse(
    os.environ.get(
        'REDIS_URL',
        'redis://localhost:6379'
    )
)
