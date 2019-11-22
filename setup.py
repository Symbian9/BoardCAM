# https://pypi.org/project/BoardCAM/

from setuptools import setup, find_packages

requires = [
    "reportlab==3.5.21",
]

with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='BoardCAM',
    version='0.0.2',
    packages=find_packages(),
    url='https://BoardCAM.org',
    license='MIT',
    author='Xiang Zheng',
    author_email='me@BoardCAM.org',
    description='snowboard ski splitboard CAD/CAM software',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requires,
)
