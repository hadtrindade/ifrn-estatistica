#!/usr/bin/python3

try:
    from setuptools import setup, find_packages

except ImportError:
    from distutils.core import setup, find_packages


def read(filename):
    return [requirement.strip() for requirement in open(filename).readlines()]


PACKAGE = "ifrn_estatistica"
NAME = "ifrn_estatistica"
DESCRIPTION = "Tabela descritiva"
AUTHOR = "Ivo Trindade"
AUTHOR_EMAIL = "haddleytrindade@gmail.com"
URL = "https://github.com/hadtrindade/ifrn-estatistica"
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    keywords="tabela descritiva",
    url=URL,
    description=DESCRIPTION,
    packeges=find_packages(
        exclude=["tests"]
        ),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={"dev": read("requirements_dev.txt")},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Framework :: Pytest",
        "Topic :: Software Development :: Testing :: Unit"

    ],
    zip_safe=False,
)