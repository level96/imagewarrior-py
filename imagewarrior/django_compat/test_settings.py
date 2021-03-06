SECRET_KEY = '123'
BASE_URL = 'https://my-hp.de'
BILDERFEE_TOKEN = 'BF_TOKEN'
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
    }
}
INSTALLED_APPS = [
    "imagewarrior.django_compat"
]
MIDDLEWARE = []
ROOT_URLCONF = "tests.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'loaders': [
                ('django.template.loaders.cached.Loader', []),
            ],
            'context_processors': [
                'imagewarrior.django_compat.context_processors.imagewarrior'
            ],
        },
    },
]
