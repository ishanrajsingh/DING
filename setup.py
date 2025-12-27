#!/usr/bin/env python3

from setuptools import setup

setup(
    name="ding",
    version="1.0",
    packages=["src"],
    entry_points={"console_scripts": ["ding = src.cli:main"]},
)
