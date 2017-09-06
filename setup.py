from setuptools import setup, find_packages

setup(
    name='whereismyjojo',
    version='0.0.1.alpha',
    description='Uber like, whereismyjojo tank.',
    author='Thapelo Tsotetsi',
    author_email='info@tsotetsithapelo.co.za',
    url='http://metsing.com',
    install_requires=[
        'Django',
        'django-model-utils',
        'djangorestframework',
        'psycopg2',
        'drfdocs==0.0.9',  # TODO: Anything above this breaks. See https://goo.gl/RgPu85
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
)
