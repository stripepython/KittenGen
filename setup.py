from setuptools import setup, find_packages

from KittenGen import version

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='KittenGen',
    packages=find_packages(exclude=(), include=('*',)),
    author='stripe-python',
    author_email='stripe-python@139.com',
    maintainer='stripe-python',
    maintainer_email='stripe-python@139.com',
    license='MIT License',
    install_requires=['flask~=3.0.3'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
    version=version,
)
