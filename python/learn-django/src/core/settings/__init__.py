import importlib
from decouple import config

# Get environment name from .env file
env = config('DJANGO_ENV', default='production')

# Import settings module
module = importlib.import_module(f'.{env}', __package__)

# Copy all uppercase variables into current namespace
for attr in dir(module):
    if attr.isupper():
        globals()[attr] = getattr(module, attr)
