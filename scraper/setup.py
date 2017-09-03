# !/usr/bin/env python

from setuptools import setup, find_packages

requires = ["scrapy"]

setup(
    name="k9-scraper",
    version="0.1",
    description="k9-scraper",
    author="Jose Guilherme Vanz",
    author_email="guilherme.sft@gmail.com",
    url="https://github.com/jvanz/k9",
    packages=find_packages(),
    requires=requires
)
