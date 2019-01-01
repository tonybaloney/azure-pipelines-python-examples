import io

from setuptools import find_packages, setup


setup(
    name='demolib',
    version='1.0.0',
    url='http://flask.pocoo.org/docs/tutorial/',
    license='MIT',
    maintainer='Anthony Shaw',
    maintainer_email='anthonyshaw@apache.org',
    description='The basic app for testing.',
    long_description="",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
