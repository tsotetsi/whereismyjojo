from setuptools import setup, find_packages

setup(
    name='metsing',
    version='0.0.1.alpha',
    description='Uber like web application for Jojo Tanks.',
    author='Thapelo Tsotetsi',
    author_email='info@tsotetsithapelo.co.za',
    url='http://metsing.com',
    install_requires=[
        'Django',
        'django-model-utils',
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
)
