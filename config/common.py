import collections
import os

DEBUG = False
ROOT_DIR = os.path.join(os.path.dirname(__file__), '..')
PROJECT_DIR = os.path.join(os.path.dirname(__file__), '../cfrweb')
STATIC_FILES_DIR = os.path.join(PROJECT_DIR, 'assets')
TEMPLATES_DIR = os.path.join(ROOT_DIR, 'cfrweb/templates')
CACHE_TIMEOUT = collections.OrderedDict([
    ('image/*', 604800),
    ('text/*', 300),
    ('*', 300)
])
