# !/usr/bin/env python

from setuptools import setup, find_packages

requires = ["scrapy"]

setup(
    name="dwarf-scraper",
    version="0.1",
    description="dwarf-scraper",
    author="Jose Guilherme Vanz",
    author_email="guilherme.sft@gmail.com",
    url="https://github.com/jvanz/dwarf",
    packages=find_packages(),
    install_requires=requires
)
