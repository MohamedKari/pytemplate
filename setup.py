from setuptools import setup, find_packages

setup(
    name="PKG_NAME",
    description="",
    author="",
    author_email="",
    url="",
    packages = find_packages(),
    install_requires = [
        "requests",
        "boto3"
    ]
)