from setuptools import setup
from os import path


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='termstrap',
    version='1.2.4',
    description='Terminal Bootstrap - A Python css file for unicode text formatting in python console output',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='t3chn0tr0n',
    author_email='technotron.avik@gmail.com',
    url='https://github.com/t3chn0tr0n/termstrap',
    py_modules=["css"],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.*.*',
    project_urls={
        'Source': 'https://github.com/t3chn0tr0n/termstrap',
    }
)
