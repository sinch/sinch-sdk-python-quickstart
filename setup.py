from setuptools import setup, find_packages

setup(
    name="sinch-sdk-python-quickstart",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # TODO: Add 'sinch' after v2.0 release.
        "flask"
    ],
    python_requires=">=3.9",
)