from setuptools import setup

setup(
    name='django-ark',
    version='0.1.4',
    packages=['ark', 'ark.migrations'],
    url='https://github.com/BlockHub/django-ark',
    license='MIT',
    author='Charles',
    author_email='karel@blockhub.nl',
    description='ark blockchain integration with Django',
    install_requires=[
        'Arky','base58', 'certifi', 'cffi', 'chardet', 'Django', 'psycopg2-binary'
        'django-compat', 'django-filter', 'docopt', 'ecdsa', 'ECPy', 'future', 'graphene',
        'graphene-django', 'graphql-core', 'graphql-relay', 'hidapi', 'idna', 'iso8601',
        'jsonfield', 'ledgerblue', 'Pillow', 'pkginfo', 'promise', 'protobuf',
        'pycparser', 'pycrypto', 'PyNaCl', 'python-dateutil', 'python-decouple', 'pytz',
        'requests', 'requests-toolbelt', 'Rx', 'singledispatch', 'six', 'tqdm',
        'typing', 'urllib3'
      ],
)
