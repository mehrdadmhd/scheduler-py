import codecs
from setuptools import setup


def read_file(filename):
    """
    Read a utf8 encoded text file and return its contents.
    """
    with codecs.open(filename, 'r', 'utf8') as f:
        return f.read()


setup(
    name='scheduler',
    packages=['scheduler'],
    description='Python task scheduling with cron expression',
    long_description=read_file('README.rst'),
    version='0.1',
    url='https://github.com/mehrdadmhd/scheduler-py',
    author='Mehrdad Mahmoudi',
    author_email='mehrdad@asiatech.ir',
    keywords=['pip','schedule','python','python3','job','cron']
)