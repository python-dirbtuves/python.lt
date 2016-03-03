from pythonlt.settigns.base import *  # noqa
from pythonlt.secretkey import get_secret_key


SECRET_KEY = get_secret_key(os.path.join(BASE_DIR, 'var', 'secretkey'))

# Keep templates in memory
del TEMPLATES[0]['APP_DIRS']
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
]

# Append the MD5 hash of the file’s content to the filename
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
