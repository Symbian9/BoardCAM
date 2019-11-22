from setuptools import setup

with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='BoardCAM',
    version='0.0.1',
    packages=['tests'],
    url='https://BoardCAM.org',
    license='MIT',
    author='Xiang Zheng',
    author_email='me@BoardCAM.org',
    description='snowboard ski splitboard CAD/CAM software',
    long_description=long_description,
    long_description_content_type="text/markdown",
)
