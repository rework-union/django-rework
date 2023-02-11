# Environ support types:
# https://django-environ.readthedocs.io/en/latest/types.html

# SECURITY WARNING: don't run with the debug turned on in production!
DEBUG=True

# Allowed hosts this Django site can serve
ALLOWED_HOSTS=example.com,127.0.0.1

# Database connection url strings (String contains `#` must urlencode)
DATABASE_URL=mysql://user:password@host:port/dbname
