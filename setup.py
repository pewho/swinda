#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='swinda',
    version="0.0.2",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    author="Mathias Bazire",
    author_email="mathias.bazire@sylpheo.com",
    description="JWT with RS256 JWA Validator tool",
    long_description=open('README.md').read(),
    install_requires=["python-jose", "requests"],
    include_package_data=True,
    url='http://github.com/pewho/swinda',
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Tool",
    ],
    entry_points={
        'console_scripts': [
            'swinda_validate = swinda.cmd:validate_jwt',
        ],
    },
    license="MIT"
)
