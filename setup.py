#!/usr/bin/env python

import setuptools

with open("README", "r") as fh:
    long_description = fh.read()

with open("LICENSE", "r") as fh:
    source_license = fh.read()

setuptools.setup(
        name='Duel Eclipse CLI',
        version='1.0.0',
        description='Generate new Duel Eclipse projects with ease',
        long_description=long_description,
        license=source_license,
        author='Duel Studios',
        author_email='admin@duel.org',
        url='https://www.github.com/duel/eclipse-cli',
        packages=setuptools.find_packages(),
        package_dir={'eclipse': 'eclipse'},
        python_requires=">=3.7",
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT",
            "Operating System :: OS Independent",
        ],
        entry_points={
            'console_scripts': ['duel-eclipse=eclipse.main:main'],
        }
    )
