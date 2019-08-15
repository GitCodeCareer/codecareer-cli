#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("LICENSE", "r") as fh:
    source_license = fh.read()

setuptools.setup(
        name='CodeCareer CLI',
        version='1.0.0',
        description='A command-line utility for interacting with CodeCareer things',
        long_description=long_description,
        license=source_license,
        author='CodeCareer',
        author_email='croc122@gmail.com',
        url='https://www.github.com/GitCodeCareer/codecareer-cli',
        packages=setuptools.find_packages(),
        package_dir={'codecareer': 'codecareer'},
        python_requires=">=3.7",
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT",
            "Operating System :: OS Independent",
        ],
        entry_points={
            'console_scripts': ['codecareer=codecareer.main:main'],
        }
    )
