from pathlib import Path
# SECRET_KEY = 'django-insecure-s)cf1c(3ss*^1fxfpq#83=l(m*z-zhrq^_on(c1#8-ypca81mf'
SECRET_KEY = 'O6B3pfZnEgAakyFXc59fc38rC2fHKO6B3pfZnEgAakyFXc59fc38SfLFpa2BAN294H'

BASE_DIR = Path(__file__).resolve().parent.parent
DbSqLite = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
     }
 }

DbMySQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'XXXXXXXXX',
        'USER': 'XXXXXXXXX',
        'PASSWORD': 'XXXXXXXXXXXXX',
        'HOST': 'XXXXXXXXXX',
        'PORT': '3306',
        # 'OPTIONS':  {
        #     'ssl': {'ca': 'C:/ssl/server-ca.pem',
        #     'cert': 'C:/ssl/client-cert.pem',
        #     'key': 'C:/ssl/client-key.pem'
        #     }
        # }
    }
}

DbPgSql= {
    
    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'XXXXXXXXX',
        'USER': 'XXXXXXXXX',
        'PASSWORD': 'XXXXXXXXX',
        'HOST': 'XXXXXXXXX',
        'PORT': '5432',

    }
}


DATABASES = DbSqLite 
# DATABASES = DbMySQL
# DATABASES = DbPgSql




