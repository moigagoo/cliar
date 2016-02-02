from setuptools import setup, find_packages

from sys import version_info


try:
    long_description = open('README.rst').read()
except:
    long_description = 'Cliar (pronounced as "clear") helps you create command-line interfaces with minimum code.'


setup(
    name='cliar',
    version='1.1.2',
    author='Konstantin Molchanov',
    description='Cliar (pronounced as "clear") helps you create command-line interfaces with minimum code.',
    long_description=long_description,
    author_email='moigagoo@live.com',
    url='https://bitbucket.org/moigagoo/cliar',
    packages=find_packages(exclude=['docs']),
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix']
)
