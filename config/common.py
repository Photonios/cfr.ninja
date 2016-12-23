import collections
import os

DEBUG = False
ROOT_DIR = os.path.join(os.path.dirname(__file__), '..')
PROJECT_DIR = os.path.join(os.path.dirname(__file__), '../cfrweb')
STATIC_FILES_DIR = os.path.join(PROJECT_DIR, 'assets')

CACHE_TIMEOUT = collections.OrderedDict([
    ('image/*', 604800),
    ('text/*', 300),
    ('*', 300)
])

TEMPLATES_DIR = os.path.join(ROOT_DIR, 'cfrweb/templates')
TEMPLATES_DEFAULT_CONTEXT = {
    'meta': {
        'description': 'Real-time updates on trains in Romania.',
        'keywords': 'CFR Romania real-time updates train'
    }
}
