from setuptools import setup, find_packages
from getpass import getuser
import os

user = getuser()

setup(
    name='auto-update',
    version='1.0.0',
    description='The Official Electric CLI For Auto-Updating Manifests',
    url='https://github.com/electric-package-manager/electric',
    author='XtremeDevX',
    author_email='xtremedevx@electric.sh',
    py_modules=['auto-update'],
    packages=find_packages(),
    scripts=[os.path.join(os.path.abspath(os.getcwd()), 'au.py')],
    install_requires=[
        'click',
        'pygments'
    ],
    entry_points='''
        [console_scripts]
        au=au:cli
    ''',
    classifiers=[
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: Windows 10",
    ]
)
