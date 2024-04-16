"""
Setup for GlobalPayments.Api
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='GlobalPayments.Api',
    version='1.0.9',
    author='Heartland Payment Systems',
    author_email='EntApp_DevPortal@e-hps.com',
    packages=[
        'python_sdk.globalpayments',
        'python_sdk.globalpayments.api',
        'python_sdk.globalpayments.api.builders',
        'python_sdk.globalpayments.api.builders.validations',
        'python_sdk.globalpayments.api.entities',
        'python_sdk.globalpayments.api.entities.table_service',
        'python_sdk.globalpayments.api.gateways',
        'python_sdk.globalpayments.api.payment_methods',
        'python_sdk.globalpayments.api.services',
        'python_sdk.globalpayments.api.utils'
    ],
    scripts=[],
    url='https://developer.heartlandpaymentsystems.com/',
    license='LICENSE.md',
    description='Global Payments Python SDK for integrating with Heartland and Global Payments merchant services APIs.',
    long_description=open('README.txt').read(),
    install_requires=[
        'xmltodict >= 0.9.0', 'jsonpickle >= 0.6.1', 'enum34 >= 1.1.6',
        'urllib3[secure] >= 1.18, <2', 'certifi >= 2016.9.26',
        'pyopenssl >= 17.5.0'
    ])
